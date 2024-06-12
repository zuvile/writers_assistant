import { Chapter as ChapterInterface } from "../api";
import { useState } from "react";

interface Props {
  chapter: ChapterInterface | null;
}

function Info({ chapter }: Props) {
  const [summaryOpen, setSummaryOpen] = useState(false);

  const onSummaryClick = () => {
    setSummaryOpen(!summaryOpen);
  };
  if (chapter === null || chapter === undefined) {
    return <div className="container">Select chapter</div>;
  }

  return (
    <div className="container">
      <div className="accordion" id="accordionExample">
        <div className="accordion-item">
          <h2 className="accordion-header">
            <button
              onClick={onSummaryClick}
              className={
                summaryOpen ? "accordion-button" : "accordion-button collapsed"
              }
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapseOne"
              aria-expanded={summaryOpen ? "true" : "false"}
              aria-controls="collapseOne"
            >
              Summary
            </button>
          </h2>
          <div
            id="collapseOne"
            className={
              summaryOpen
                ? "accordion-collapse collapse show"
                : "accordion-collapse collapse"
            }
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <p>{chapter.summary}</p>
            </div>
          </div>
        </div>
      </div>
      <div className="container">
        <p>
          Word count:
          <span className="badge bg-secondary"> {chapter.word_count} </span>
        </p>
        <h2>
          <span className="badge bg-secondary">Characters</span>
        </h2>

        <ul className="list-group">
          {chapter.characters.map((character) => (
            <li className="list-group-item" key={character.id}>
              {character.name}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Info;
