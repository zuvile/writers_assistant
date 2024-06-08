import { getToken } from "./auth";
import axios from "axios";
import chapter from "./components/Chapter";

export interface Novel {
  id: number;
  novel_name: string;
  genre: string;
  word_count: number;
  upload_date: string;
}

export interface FileUpload {
  title: string;
  genre: string;
  file: File;
}

export interface Character {
  id: number;
  name: string;
  age: number;
  gender: string;
  description: string;
}

export interface Paragraph {
  id: number;
  text: string;
  is_dialogue: boolean;
}

export interface Chapter {
  id: number;
  title: string;
  number: number;
  word_count: number;
}

export interface Scene {
  id: number;
}

export async function fetchCharacters() {
  try {
    const token = getToken();
    const response = await axios.get(
      "http://127.0.0.1:8000/assistant/api/novels/characters/",
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

export async function fetchChapters(novel_id: number) {
  try {
    const token = getToken();
    const response = await axios.get(
      "http://127.0.0.1:8000/assistant/api/novels/" + novel_id + "/chapters/",
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      },
    );
    return response.data;
  } catch (error) {
    console.error("Error fetching chapters:", error);
    return [];
  }
}

export async function fetchParagraphs(
  novel_id: number,
  chapter_id: number,
  scene_id: number,
) {
  try {
    const token = getToken();
    const response = await axios.get(
      "http://127.0.0.1:8000/assistant/api/novels/" +
        novel_id +
        "/chapters/" +
        chapter_id +
        "/scenes/" +
        scene_id +
        "/paragraphs/",
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      },
    );
    return response.data;
  } catch (error) {
    console.error("Error fetching paragraphs:", error);
    return [];
  }
}

export async function deleteNovel(novel_id: number) {
  try {
    const token = getToken();
    const response = await axios.delete(
      "http://127.0.0.1:8000/assistant/api/novels/" + novel_id + "/",
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      },
    );
    return response.data;
  } catch (error) {
    console.error("Error deleting novel:", error);
    return [];
  }
}

export async function fetchScenes(novel_id: number, chapter_id: number) {
  try {
    const token = getToken();
    const response = await axios.get(
      "http://127.0.0.1:8000/assistant/api/novels/" +
        novel_id +
        "/chapters/" +
        chapter_id +
        "/scenes/",
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      },
    );
    return response.data;
  } catch (error) {
    console.error("Error fetching scenes:", error);
    return [];
  }
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

export async function createCharacter(
  name: string,
  age: number,
  description: string,
  gender: string,
  novels: number[],
) {
  const token = getToken();
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/assistant/api/novels/characters/",
      {
        name: name,
        age: age,
        description: description,
        gender: gender,
        novels: novels,
      },
      {
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "application/json",
        },
      },
    );
    return response.data;
  } catch (error) {
    console.error("Error creating character", error);
    return [];
  }
}

export async function uploadNovel({ title, genre, file }: FileUpload) {
  const token = getToken();
  console.log(file, title);
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/assistant/api/novels/upload/",
      {
        file_uploaded: file,
        novel_title: title,
        genre: genre,
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

export async function regenCharacterPortrait(character_id: number) {
  try {
    const token = getToken();
    const response = await axios.post(
      "http://127.0.0.1:8000/assistant/api/novels/characters/" +
        character_id +
        "/portraits/",
      {},
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      },
    );
    return response.data["url"];
  } catch (error) {
    console.error("Error fetching chapters:", error);
    return [];
  }
}

export async function deleteCharacter(character_id: number) {
  try {
    const token = getToken();
    const response = await axios.delete(
      "http://127.0.0.1:8000/assistant/api/novels/characters/" +
        character_id +
        "/",
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      },
    );
    return response.data;
  } catch (error) {
    console.error("Error deleting novel:", error);
    return [];
  }
}
