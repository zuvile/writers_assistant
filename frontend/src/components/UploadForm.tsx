import React, { ChangeEvent, FormEvent, CSSProperties, useState } from "react";
import { fetchNovels, uploadNovel } from "../api";
import ClipLoader from "react-spinners/ClipLoader";
import RingLoader from "react-spinners/RingLoader";

interface Props {
  onUpload: () => void;
}

const UploadForm: React.FC<Props> = ({ onUpload }: Props) => {
  const [title, setTitle] = useState<string>("");
  const [file, setFile] = useState<File | null>(null);
  const [genre, setGenre] = useState("");
  const [error, setError] = useState<string>("");
  const [uploading, setUploading] = useState(false);
  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setUploading(true);
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

  const override: CSSProperties = {
    display: "block",
    margin: "0 auto",
    borderColor: "red",
  };

  const handleFileChange = function (e: React.ChangeEvent<HTMLInputElement>) {
    const fileList = e.target.files;
    if (!fileList) return;

    setFile(fileList[0]);
  };

  if (uploading) {
    return (
      <>
        <span className="align-middle">
          Uploading and generating content...
        </span>
        <RingLoader
          color={"#2471A3"}
          loading={uploading}
          cssOverride={override}
          size={150}
          aria-label="Loading Spinner"
          data-testid="loader"
        />
      </>
    );
  }

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
