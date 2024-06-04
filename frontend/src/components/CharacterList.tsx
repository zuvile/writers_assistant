import React, { ChangeEvent, useEffect, useState } from "react";
import { fetchCharacters } from "../api";
import Char from "./Char";
import { Character, fetchNovels, Novel, createCharacter } from "../api";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";

function CharacterList() {
  const [characters, setCharacters] = useState<Character[]>([]);
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  const [novels, setNovels] = useState<Novel[]>([]);
  const [selectedNovelIds, setSelectedNovelIds] = useState<number[]>([]);
  const [newCharacterName, setNewCharacterName] = useState("");

  const handleOnNovelChange = (novelId: number) => {
    if (selectedNovelIds.includes(novelId)) {
      setSelectedNovelIds(selectedNovelIds.filter((id) => id !== novelId));
    } else {
      setSelectedNovelIds([...selectedNovelIds, novelId]);
    }
  };

  const handleSave = () => {
    createCharacter(newCharacterName, selectedNovelIds).then(() => {
      fetchCharacters().then(setCharacters);
    });

    handleClose();
  };

  const handleInputChange =
    (setState: React.Dispatch<React.SetStateAction<string>>) =>
    (event: ChangeEvent<HTMLInputElement>) =>
      setState(event.target.value);

  useEffect(() => {
    fetchCharacters().then(setCharacters);
    fetchNovels().then(setNovels);
  }, []);

  return (
    <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Create new character</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <form>
            <input
              type="text"
              className="form-control"
              placeholder="Character name"
              onChange={handleInputChange(setNewCharacterName)}
            />
            <ul className="list-group">
              <br></br>
              {novels.map((novel) => (
                <li className="list-group-item" key={novel.id}>
                  <input
                    className="form-check-input me-1"
                    type="checkbox"
                    value=""
                    aria-label="..."
                    onChange={() => handleOnNovelChange(novel.id)}
                  />
                  {novel.novel_name}
                </li>
              ))}
            </ul>
          </form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="primary" onClick={handleSave}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
      <div className="container">
        <h2>Characters</h2>
        <button type="button" className="btn btn-info" onClick={handleShow}>
          Add new character
        </button>
        <hr></hr>
        <div className="row">
          {characters.map((character) => (
            <Char character={character}></Char>
          ))}
        </div>
      </div>
    </>
  );
}

export default CharacterList;
