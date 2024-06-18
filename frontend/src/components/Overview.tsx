import NovelSelect from "./NovelSelect";
import { fetchChapters, fetchNovels, Novel, Chapter } from "../api";
import { useEffect, useState } from "react";
import BarChart from "./BarChart";

interface WordCountData {
  labels: string[];
  datasets: {
    label: string;
    data: number[];
    backgroundColor: string[];
    borderColor: string;
    borderWidth: number;
  }[];
}

function Overview() {
  const [selectedNovel, setSelectedNovel] = useState<Novel>();
  const [novels, setNovels] = useState<Novel[]>([]);
  const [wordCountData, setWordCountData] = useState<
    WordCountData | undefined
  >();

  useEffect(() => {
    fetchNovels().then(setNovels);
  }, []);

  const onNovelSelect = (eventKey: string | null) => {
    if (eventKey !== null) {
      const novel = novels.find((novel) => novel.id === parseInt(eventKey));
      if (novel) {
        setSelectedNovel(novel);
        fetchChapters(novel.id).then((chapters) => {
          const newLabels = chapters.map((chapter: Chapter) =>
            chapter.title ? chapter.title : "Chapter " + chapter.number,
          );
          const newData = chapters.map(
            (chapter: Chapter) => chapter.word_count,
          );
          setWordCountData({
            labels: newLabels, // Use newLabels directly here
            datasets: [
              {
                label: "Word count",
                data: newData,
                backgroundColor: [
                  "rgba(75,192,192,1)",
                  "#ecf0f1",
                  "#50AF95",
                  "#f3ba2f",
                  "#2a71d0",
                ],
                borderColor: "black",
                borderWidth: 2,
              },
            ],
          });
        });
      }
    }
  };

  return (
    <div className="container">
      <h1>Overview</h1>
      <NovelSelect
        onNovelSelect={onNovelSelect}
        novels={novels}
        selectedNovel={selectedNovel}
      />
      <hr></hr>
      {wordCountData && (
        <>
          <h2>Word count per chapter</h2>
          <div className="bar" style={{ width: "100%" }}>
            <BarChart chartData={wordCountData} />
          </div>
        </>
      )}
    </div>
  );
}

export default Overview;
