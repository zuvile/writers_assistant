import { ReactNode, useState } from "react";
import { isLoggedIn } from "../auth";

interface Props {
  onSelectOption: (item: string) => void;
}

const navOptions = ["Home", "Bookshelf", "Overview", "Evaluate", "Logout"];

const navOptionsLoggedOut = ["Home", "Login"];

function NavBar({ onSelectOption }: Props) {
  const [selectedOption, setSelectedOption] = useState("Home");
  let options = [];
  if (isLoggedIn()) {
    options = navOptions;
  } else {
    options = navOptionsLoggedOut;
  }
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <a className="navbar-brand">Writer's Assistant</a>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            {options.map((option, index) => (
              <li
                key={option}
                className={
                  selectedOption === option ? "nav-link active" : "nav-link"
                }
                onClick={() => {
                  onSelectOption(option);
                }}
              >
                {option}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </nav>
  );
}
export default NavBar;
