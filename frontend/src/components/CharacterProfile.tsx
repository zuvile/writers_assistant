import { Character } from "../api";
import React, { useEffect, useState } from "react";
import { fetchCharacterPortrait, regenCharacterPortrait } from "../api";
import RingLoader from "react-spinners/RingLoader";

interface Props {
  character: Character;
  onDelete: (id: number) => void;
  onRegen: (id: number) => void;
}

function CharacterProfile({ character, onDelete, onRegen }: Props) {
  const [characterPortrait, setCharacterPortrait] = useState();
  const [portraitLoading, setPortraitLoading] = useState(false);

  useEffect(() => {
    fetchCharacterPortrait(character.id).then((url) => {
      setCharacterPortrait(url);
    });
  }, []);

  const onRegenerateImage = async (id: number) => {
    setPortraitLoading(true);
    const url = await fetchCharacterPortrait(id);
    await regenCharacterPortrait(id);
    const newUrl = await fetchCharacterPortrait(character.id);
    setCharacterPortrait(newUrl);
    onRegen(id);
    setPortraitLoading(false);
  };

  let portrait;

  if (portraitLoading) {
    portrait = (
      <div className="container">
        <RingLoader
          color={"#2471A3"}
          loading={portraitLoading}
          size={150}
          aria-label="Loading Spinner"
          data-testid="loader"
        />
      </div>
    );
  } else {
    portrait = (
      <img
        src={characterPortrait}
        className="object-fit-sm-contain"
        alt="..."
      />
    );
  }
  return (
    <div key={character.id} className="card" style={{ width: "14rem" }}>
      {portrait}
      <div className="card-body">
        <h5 className="card-title">{character.name}</h5>
        <p className="card-text">
          Age: {character.age}
          <br></br>
          Description: {character.description}
          <span></span>
        </p>
        <div className="btn-group" role="group" aria-label="Basic example">
          <button
            type="button"
            className="btn btn-info"
            onClick={() => {
              onRegenerateImage(character.id);
            }}
          >
            Regenerate profile picture
          </button>
          <button
            type="button"
            className="btn btn-danger"
            onClick={() => {
              onDelete(character.id);
            }}
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
}

export default CharacterProfile;
