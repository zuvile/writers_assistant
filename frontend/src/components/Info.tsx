import { useEffect, useState } from "react";
import { Character, fetchCharacters } from "../api";
import ChatbotComponent from "./ChatbotComponent";
function Info() {
  const [characters, setCharacters] = useState<Character[]>([]);

  useEffect(() => {
    fetchCharacters().then(setCharacters);
  }, []);

  const [statsOpen, setStatsOpen] = useState(false);
  const [charactersOpen, setCharactersOpen] = useState(false);

  return (
    <>
      <ChatbotComponent></ChatbotComponent>
      <div className="accordion" id="accordionExample">
        <br></br>
        <div className="accordion-item">
          <h2 className="accordion-header">
            <button
              className={
                charactersOpen
                  ? "accordion-button"
                  : "accordion-button collapsed"
              }
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapseOne"
              aria-expanded="true"
              aria-controls="collapseOne"
              onClick={() => setCharactersOpen(!charactersOpen)}
            >
              Characters
            </button>
          </h2>
          <div
            id="collapseOne"
            className={
              charactersOpen
                ? "accordion-collapse collapse show"
                : "accordion-collapse collapse"
            }
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <ul className="list-group">
                {characters.map((character) => (
                  <li className="list-group-item">
                    {character.name}
                    <img
                      src="/default_profile_pic.jpg"
                      className="rounded-circle"
                      width={20}
                      height={30}
                      alt="img"
                    />
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
        <div className="accordion-item">
          <h2 className="accordion-header">
            <button
              className={
                statsOpen ? "accordion-button" : "accordion-button collapsed"
              }
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapseTwo"
              aria-expanded="false"
              aria-controls="collapseTwo"
              onClick={() => setStatsOpen(!statsOpen)}
            >
              Stats
            </button>
          </h2>
          <div
            id="collapseTwo"
            className={
              statsOpen
                ? "accordion-collapse collapse show"
                : "accordion-collapse collapse"
            }
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">Word count: 1000</div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Info;
