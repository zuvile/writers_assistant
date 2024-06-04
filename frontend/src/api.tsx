import { getToken } from "./auth";
import axios from "axios";

export interface Novel {
  id: number;
  novel_name: string;
  word_count: number;
  upload_date: string;
}

export interface FileUpload {
  title: string;
  file: File;
}

export async function fetchNovels() {
  const token = getToken();
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/assistant/api/novels/",
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      },
    );
    return response.data;
  } catch (error) {
    console.error("Error fetching novels:", error);
    return [];
  }
}

export async function uploadNovel({ title, file }: FileUpload) {
  const token = getToken();
  console.log(file, title);
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/assistant/api/novels/upload/",
      {
        file_uploaded: file,
        novel_title: title,
      },
      {
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "multipart/form-data",
        },
      },
    );
    return response.data;
  } catch (error) {
    console.error("Error fetching novels:", error);
    return [];
  }
}
