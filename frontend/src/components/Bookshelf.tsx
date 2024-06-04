import React, { useEffect, useState } from "react";
import { fetchNovels, Novel } from "../api";
import UploadForm from "./UploadForm";

interface Props {
  onEvaluate: (id: number) => void;
}

function Bookshelf({ onEvaluate }: Props) {
  const [novels, setNovels] = useState<Novel[]>([]);

  useEffect(() => {
    fetchNovels().then(setNovels);
  }, []);

  return (
    <div className="container-fluid">
      <div className="row">
        <div className="col-sm-6 d-flex justify-content-center">
          {novels.map((novel) => (
            <div key={novel.id} className="card" style={{ width: "400px" }}>
              <img
                src="/default_novel_cover.jpg"
                className="card-img-top"
                alt="..."
              />
              <div className="card-body">
                <h5 className="card-title">{novel.novel_name}</h5>
                <p className="card-text">
                  <p>Word count: {novel.word_count.toLocaleString()}</p>
                  <p>
                    Uploaded at:{" "}
                    {new Date(novel.upload_date).toLocaleDateString()}
                  </p>
                </p>
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => {
                    onEvaluate(novel.id);
                  }}
                >
                  Evaluate
                </button>
              </div>
            </div>
          ))}
          <div key="new_novel" className="card" style={{ width: "400px" }}>
            <i className="bi bi-plus"></i>
            <div className="card-body">
              <h5 className="card-title">Add new novel</h5>
              <button type="button" className="btn btn-primary">
                <UploadForm></UploadForm>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Bookshelf;
