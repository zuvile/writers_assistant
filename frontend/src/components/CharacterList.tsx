import React, { useEffect, useState } from "react";
import { fetchCharacters } from "../api";
import Char from "./Char";
import { Character } from "../api";
import UploadForm from "./UploadForm";
function CharacterList() {
  const [characters, setCharacters] = useState<Character[]>([]);

  useEffect(() => {
    fetchCharacters().then(setCharacters);
  }, []);

  return (
    <div className="container">
      <h2>Characters</h2>
      <button type="button" className="btn btn-info">
        Add new character
      </button>
      <hr></hr>
      <div className="row">
        {characters.map((character) => (
          <Char character={character}></Char>
        ))}
      </div>
    </div>
  );
}

export default CharacterList;
