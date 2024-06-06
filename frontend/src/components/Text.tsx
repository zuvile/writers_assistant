import { useEffect, useState } from "react";
import {
  Chapter as ChapterInterface,
  Paragraph,
  Scene,
  fetchParagraphs,
  fetchNovels,
} from "../api";

interface Props {
  novelId?: number;
  chapterId: number;
  sceneIds: number[];
}

function Text({ novelId, chapterId, sceneIds }: Props) {
  const [paragraphs, setParagraphs] = useState<Paragraph[]>([]);

  useEffect(() => {
    if (!chapterId || !sceneIds || !novelId) {
      return;
    }
    let newParagraphArray: Paragraph[] = [];
    const fetchAllParagraphs = async () => {
      for (const sceneId of sceneIds) {
        const data = await fetchParagraphs(novelId, chapterId, sceneId);
        for (const paragraph of data) {
          const newParagraph = {
            id: paragraph.id,
            text: paragraph.text,
            is_dialogue: paragraph.is_dialogue,
          };
          newParagraphArray.push(newParagraph);
        }
      }
      // Sort paragraphs by id
      newParagraphArray.sort((a, b) => a.id - b.id);
      setParagraphs(newParagraphArray);
    };
    fetchAllParagraphs();
  }, [novelId, chapterId, sceneIds]);

  if (paragraphs.length === 0) {
    return <div>Such empty</div>;
  }

  return (
    <div className="overflow-auto p-3 bg-body-tertiary">
      {paragraphs.map((paragraph) => (
        <div key={paragraph.id}>
          <p>{paragraph.text}</p>
        </div>
      ))}
    </div>
  );
}

export default Text;
