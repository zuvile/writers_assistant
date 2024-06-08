import React, { useEffect, useState } from "react";
import { fetchNovels, Novel } from "../api";
import UploadForm from "./UploadForm";
import Modal from "react-bootstrap/Modal";
import { deleteNovel } from "../api";

interface Props {
  onEvaluate: (id: number) => void;
}

function Bookshelf({ onEvaluate }: Props) {
  const [novels, setNovels] = useState<Novel[]>([]);
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  useEffect(() => {
    fetchNovels().then(setNovels);
  }, []);

  const onUpload = () => {
    fetchNovels().then(setNovels);
    handleClose();
  };

  const onDelete = (novel_id: number) => {
    deleteNovel(novel_id).then(() => {
      fetchNovels().then(setNovels);
    });
  };

  return (
    <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Upload new novel</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <UploadForm onUpload={onUpload}></UploadForm>
        </Modal.Body>
      </Modal>
      <div className="container">
        <button type="button" className="btn btn-info" onClick={handleShow}>
          Add new novel
        </button>
        <br></br>
        <div className="row">
          <div className="col d-flex justify-content-center">
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
                    Word count: {novel.word_count.toLocaleString()}
                    <br></br>
                    Uploaded at:
                    {new Date(novel.upload_date).toLocaleDateString()}
                  </p>
                  <div
                    className="btn-group"
                    role="group"
                    aria-label="Basic example"
                  >
                    <button
                      type="button"
                      className="btn btn-primary"
                      onClick={() => {
                        onEvaluate(novel.id);
                      }}
                    >
                      Evaluate
                    </button>
                    <button
                      type="button"
                      className="btn btn-danger"
                      onClick={() => {
                        onDelete(novel.id);
                      }}
                    >
                      Delete
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}

export default Bookshelf;
