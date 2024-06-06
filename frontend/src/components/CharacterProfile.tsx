import { Character } from "../api";

interface Props {
  character: Character;
}

function CharacterProfile({ character }: Props) {
  return (
    <div key={character.id} className="card" style={{ width: "14rem" }}>
      <img
        src="/default_profile_pic.jpg"
        className="object-fit-sm-contain"
        alt="..."
      />
      <div className="card-body">
        <h5 className="card-title">{character.name}</h5>
        <p className="card-text">
          Age: {character.age}
          <br></br>
          Description: {character.description}
          <span></span>
        </p>
      </div>
    </div>
  );
}
export default CharacterProfile;
