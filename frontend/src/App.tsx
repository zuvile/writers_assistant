import { useState } from "react";
import NavBar from "./components/NavBar";
import Novel from "./components/Novel";
import Bookshelf from "./components/Bookshelf";
import Overview from "./components/Overview";
import HomePage from "./components/HomePage";

function App() {
  let items = ["Chapter 1", "Chapter 2", "Chapter 3"];

  const [selectedOption, setSelectedOption] = useState("Home");
  const onSelectOption = (option: string) => {
    setSelectedOption(option);
  };
  return (
    <div>
      <NavBar onSelectOption={onSelectOption}></NavBar>
      {selectedOption === "Home" && <HomePage></HomePage>}
      {selectedOption === "Bookshelf" && <Bookshelf></Bookshelf>}
      {selectedOption === "Evaluate" && <Novel></Novel>}
      {selectedOption === "Overview" && <Overview></Overview>}
    </div>
  );
}

export default App;
