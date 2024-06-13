import Dropdown from "react-bootstrap/Dropdown";
import { Novel } from "../api";

interface Props {
  onNovelSelect: (eventKey: string | null) => void;
  novels: Novel[];
  selectedNovel?: Novel | null;
}

function NovelSelect({ onNovelSelect, novels, selectedNovel }: Props) {
  return (
    <div className="container">
      <Dropdown onSelect={onNovelSelect}>
        <Dropdown.Toggle variant="success" id="dropdown-basic">
          {selectedNovel?.novel_name || "Select a novel"}
        </Dropdown.Toggle>
        <Dropdown.Menu>
          {novels.map((novel) => (
            <Dropdown.Item
              key={novel.id}
              eventKey={novel.id}
              active={selectedNovel?.id === novel.id}
            >
              {novel.novel_name}
            </Dropdown.Item>
          ))}
        </Dropdown.Menu>
      </Dropdown>
    </div>
  );
}
export default NovelSelect;
