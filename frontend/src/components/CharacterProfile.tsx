import { Character } from "../api";
import React, { useEffect, useState } from "react";
import {
  regenCharacterPortrait,
  patchCharacter,
  PartialCharacter,
} from "../api";
import RingLoader from "react-spinners/RingLoader";
import { BASE_URL } from "../config";
import { InlineEdit, Input } from "rsuite";

interface Props {
  character: Character;
  onDelete: (id: number) => void;
  onRegen: (id: number) => void;
}

function CharacterProfile({ character, onDelete, onRegen }: Props) {
  const [characterPortrait, setCharacterPortrait] = useState("");
  const [portraitLoading, setPortraitLoading] = useState(false);

  const onNameChange = (value: string) => {
    let partialCharacter: PartialCharacter = {
      id: character.id,
      name: value,
    };

    patchCharacter(partialCharacter);
  };

  const onDescriptionChange = (value: string) => {
    let partialCharacter: PartialCharacter = {
      id: character.id,
      description: value,
    };

    patchCharacter(partialCharacter);
  };

  const onAgeChange = (value: number) => {
    let partialCharacter: PartialCharacter = {
      id: character.id,
      age: value,
    };

    patchCharacter(partialCharacter);
  };

  useEffect(() => {
    fetchCharacterPortrait(character.id);
  }, []);

  const fetchCharacterPortrait = (id: number) => {
    // Add timestamp to url to prevent caching
    const timestamp = new Date().getTime();
    const url = `${BASE_URL}assistant/api/novels/characters/${id}/current_portrait/?${timestamp}`;
    setCharacterPortrait(url);
  };

  const onRegenerateImage = async (id: number) => {
    setPortraitLoading(true);
    await regenCharacterPortrait(id);
    fetchCharacterPortrait(character.id);
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
        <h5 className="card-title">
          <InlineEdit defaultValue={character.name} onChange={onNameChange} />
        </h5>
        <p className="card-text">
          <InlineEdit defaultValue={character.age} onChange={onAgeChange} />
          <br></br>
          <InlineEdit
            defaultValue={character.description}
            onChange={onDescriptionChange}
          >
            <Input as="textarea" rows={5} style={{ width: "100%" }} />
          </InlineEdit>
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
