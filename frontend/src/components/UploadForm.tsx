import React, { ChangeEvent, FormEvent, useEffect, useState } from "react";
import { fetchNovels, uploadNovel } from "../api";
import { Tooltip } from "react-tooltip";

interface Props {
  onUpload: () => void;
}

const UploadForm: React.FC<Props> = ({ onUpload }: Props) => {
  const [title, setTitle] = useState<string>("");
  const [file, setFile] = useState<File | null>(null);
  const [genre, setGenre] = useState("");
  const [error, setError] = useState<string>("");

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();

    if (file) {
      try {
        const result = await uploadNovel({ title, genre, file });
        onUpload();
      } catch (error) {
        setError("Invalid title or file");
      }
    }
  };

  const handleInputChange =
    (setState: React.Dispatch<React.SetStateAction<string>>) =>
    (event: ChangeEvent<HTMLInputElement>) =>
      setState(event.target.value);

  const handleFileChange = function (e: React.ChangeEvent<HTMLInputElement>) {
    const fileList = e.target.files;
    if (!fileList) return;

    setFile(fileList[0]);
  };

  return (
    <div className="container">
      <form>
        <br></br>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            id="novel title"
            placeholder="Novel title"
            onChange={handleInputChange(setTitle)}
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            id="genre"
            placeholder="Novel genre"
            onChange={handleInputChange(setGenre)}
          />
        </div>
        <div className="mb-3">
          <input
            className="form-control"
            type="file"
            id="formFile"
            onChange={handleFileChange}
          />
        </div>
        <div className="form-check">
          <input
            className="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckChecked"
            checked
          />
          <label className="form-check-label" htmlFor="flexCheckChecked">
            Generate AI content
          </label>
        </div>
        <button
          className="btn btn-primary"
          type="submit"
          onClick={handleSubmit}
        >
          Submit
        </button>
      </form>
    </div>
  );
};
export default UploadForm;
