import Chapter from "./Chapter";
import Text from "./Text";
import Info from "./Info";
import { useEffect, useState } from "react";
import {
  fetchNovels,
  Novel as NovelInterface,
  Chapter as ChapterInterface,
  fetchChapters,
  fetchScenes,
  Scene,
  Character,
} from "../api";
import Dropdown from "react-bootstrap/Dropdown";
import NovelSelect from "./NovelSelect";

function Novel() {
  const [novels, setNovels] = useState<NovelInterface[]>([]);
  const [selectedNovel, setSelectedNovel] = useState<NovelInterface | null>(
    null,
  );
  const [chapters, setChapters] = useState<ChapterInterface[]>([]);
  const [selectedChapterId, setSelectedChapterId] = useState(0);
  const [sceneIds, setSceneIds] = useState<number[]>([]);
  const [currentChapter, setCurrentChapter] = useState<ChapterInterface | null>(
    null,
  );

  const onChapterSelect = async (chapterId: number | null) => {
    if (chapterId !== null) {
      const scenes = await fetchScenes(selectedNovel?.id || 0, chapterId);
      const newSceneIds = scenes.map((scene: Scene) => scene.id);
      setSceneIds(newSceneIds);
      setSelectedChapterId(chapterId);
      chapters.forEach((chapter) => {
        if (chapter.id === chapterId) {
          setCurrentChapter(chapter);
        }
      });
    }
  };

  useEffect(() => {
    fetchNovels().then(setNovels);
    setSelectedNovel(novels[0]);
  }, [sceneIds, selectedChapterId]);

  const onNovelSelect = (eventKey: string | null) => {
    if (eventKey !== null) {
      const novel = novels.find((novel) => novel.id === parseInt(eventKey));
      if (novel) {
        setSelectedNovel(novel);
        fetchChapters(novel.id).then(setChapters);
      }
    }
  };

  return (
    <div className="container">
      <br></br>
      <NovelSelect
        onNovelSelect={onNovelSelect}
        novels={novels}
        selectedNovel={selectedNovel}
      ></NovelSelect>
      <div className="row">
        <div className="col">
          <div className="d-flex flex-column vh-100 overflow-auto">
            <h1>Chapters</h1>
            {chapters.map((chapter) => (
              <Chapter
                key={chapter.id}
                chapter={chapter}
                selectedChapterId={selectedChapterId}
                onChapterSelect={onChapterSelect}
              ></Chapter>
            ))}
          </div>
        </div>
        <div className="col-8">
          <div className="d-flex flex-column vh-100 overflow-auto">
            <h1>Text</h1>
            <Text
              key={selectedChapterId}
              novelId={selectedNovel?.id}
              chapterId={selectedChapterId}
              sceneIds={sceneIds}
            ></Text>
          </div>
        </div>
        <div className="col">
          <div className="d-flex flex-column vh-100 overflow-auto">
            <h1>Info</h1>
            <Info chapter={currentChapter}></Info>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Novel;
