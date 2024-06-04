import React, { ChangeEvent, FormEvent, useEffect, useState } from "react";
import { fetchNovels, uploadNovel } from "../api";
import axios from "axios";

const UploadForm: React.FC = () => {
  const [title, setTitle] = useState<string>("");
  const [file, setFile] = useState<File | null>(null);
  const [error, setError] = useState<string>("");

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    console.log(title, file);

    if (file) {
      try {
        const result = await uploadNovel({ title, file });
        console.log(result);
      } catch (error) {
        console.log(error);
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
            className="form-control"
            type="file"
            id="formFile"
            onChange={handleFileChange}
          />
        </div>
        <button type="submit" onClick={handleSubmit}>
          Submit
        </button>
      </form>
    </div>
  );
};
export default UploadForm;
