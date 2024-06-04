import { Character } from "../api";

interface Props {
  character: Character;
}

function Char({ character }: Props) {
  return (
    <div className="card" style={{ width: "14rem" }}>
      <img
        src="/default_profile_pic.jpg"
        className="object-fit-sm-contain"
        alt="..."
      />
      <div className="card-body">
        <h5 className="card-title">{character.name}</h5>
        <p className="card-text">
          <span>TODO other info</span>
          <br></br>
          <span></span>
        </p>
      </div>
    </div>
  );
}
export default Char;
