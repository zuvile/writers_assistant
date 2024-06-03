import Chapter from "./Chapter";
import Text from "./Text";
import Info from "./Info";

function Novel() {
  return (
    <div className="container">
      <div className="dropdown">
        <button
          className="btn btn-secondary dropdown-toggle"
          type="button"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >
          Novel Title
        </button>
        <ul className="dropdown-menu">
          <li>
            <a className="dropdown-item" href="#">
              Novel title
            </a>
          </li>
        </ul>
      </div>
      <div className="row">
        <div className="col">
          <h1>Chapters</h1>
          <Chapter></Chapter>
          <Chapter></Chapter>
          <Chapter></Chapter>
        </div>
        <div className="col-8">
          <h1>Text</h1>
          <Text></Text>
        </div>
        <div className="col">
          <h1>Info</h1>
          <Info></Info>
        </div>
      </div>
    </div>
  );
}

export default Novel;
