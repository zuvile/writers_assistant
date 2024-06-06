import React, { ChangeEvent, useEffect, useState } from "react";
import { fetchCharacters } from "../api";
import CharacterProfile from "./CharacterProfile";
import {
  Character,
  fetchNovels,
  Novel,
  createCharacter,
  deleteCharacter,
} from "../api";
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
  const [newCharacterAge, setNewCharacterAge] = useState(0);
  const [newCharacterDescription, setNewCharacterDescription] = useState("");

  const handleOnNovelChange = (novelId: number) => {
    if (selectedNovelIds.includes(novelId)) {
      setSelectedNovelIds(selectedNovelIds.filter((id) => id !== novelId));
    } else {
      setSelectedNovelIds([...selectedNovelIds, novelId]);
    }
  };

  const handleSave = () => {
    createCharacter(
      newCharacterName,
      newCharacterAge,
      newCharacterDescription,
      selectedNovelIds,
    ).then(() => {
      fetchCharacters().then(setCharacters);
    });

    handleClose();
  };

  const onDelete = (id: number) => {
    deleteCharacter(id).then(() => {
      fetchCharacters().then(setCharacters);
    });
  };

  const handleInputChange =
    (setState: React.Dispatch<React.SetStateAction<string>>) =>
    (event: ChangeEvent<HTMLInputElement>) =>
      setState(event.target.value);

  const handleNumberInputChange =
    (setState: React.Dispatch<React.SetStateAction<number>>) =>
    (event: React.ChangeEvent<HTMLInputElement>) => {
      setState(Number(event.target.value));
    };

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
            <input
              type="number"
              className="form-control"
              placeholder="Character age"
              onChange={handleNumberInputChange(setNewCharacterAge)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="Character description"
              onChange={handleInputChange(setNewCharacterDescription)}
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
            <CharacterProfile
              character={character}
              onDelete={onDelete}
            ></CharacterProfile>
          ))}
        </div>
      </div>
    </>
  );
}

export default CharacterList;
