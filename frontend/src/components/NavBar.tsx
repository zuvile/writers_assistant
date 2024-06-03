import { ReactNode, useState } from "react";

interface Props {
  onSelectOption: (item: string) => void;
}

const navOptions = ["Home", "Bookshelf", "Overview", "Evaluate"];

function NavBar({ onSelectOption }: Props) {
  const [selectedOption, setSelectedOption] = useState("Home");

  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          Writer's Assistant
        </a>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            {navOptions.map((option, index) => (
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
