import { Chapter as ChapterInterface } from "../api";
import { useState } from "react";

interface Props {
  chapter: ChapterInterface;
  selectedChapterId: number;
  onChapterSelect: (chapterId: number | null) => void;
}

function Chapter({ chapter, selectedChapterId, onChapterSelect }: Props) {
  const chapterOpen = chapter.id === selectedChapterId; // Check if this chapter is the open chapter

  const handleChapterSelect = (chapter: ChapterInterface) => {
    if (!chapterOpen) {
      onChapterSelect(chapter.id);
    }
  };

  return (
    <div>
      <div className="accordion" id="accordionExample">
        <div className="accordion-item">
          <h2 className="accordion-header">
            <button
              className={
                chapterOpen ? "accordion-button" : "accordion-button collapsed"
              }
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapseTwo"
              aria-expanded="false"
              aria-controls="collapseTwo"
              onClick={() => handleChapterSelect(chapter)}
            >
              {getChapterName(chapter)}
            </button>
          </h2>
          <div
            id="collapseTwo"
            className={
              chapterOpen
                ? "accordion-collapse collapse show"
                : "accordion-collapse collapse"
            }
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              Word count: {chapter.word_count}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Chapter;

function getChapterName(chapter: ChapterInterface) {
  let chapterName = "";
  if (chapter.title !== "" && chapter.number !== -1) {
    chapterName = chapter.number + " " + chapter.title;
  } else if (chapter.number !== -1) {
    chapterName = chapter.number + " " + "Chapter";
  } else {
    chapterName = "Prologue";
  }

  return chapterName;
}
