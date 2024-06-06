import { Character } from "../api";
import React from "react";

interface Props {
  character: Character;
  onDelete: (id: number) => void;
}

function CharacterProfile({ character, onDelete }: Props) {
  return (
    <div key={character.id} className="card" style={{ width: "14rem" }}>
      <img
        src="/default_profile_pic.jpg"
        className="object-fit-sm-contain"
        alt="..."
      />
      <div className="card-body">
        <h5 className="card-title">{character.name}</h5>
        <p className="card-text">
          Age: {character.age}
          <br></br>
          Description: {character.description}
          <span></span>
        </p>
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
  );
}

export default CharacterProfile;
