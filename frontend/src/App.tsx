import { useState, useEffect } from "react";
import NavBar from "./components/NavBar";
import Novel from "./components/Novel";
import Bookshelf from "./components/Bookshelf";
import Overview from "./components/Overview";
import HomePage from "./components/HomePage";
import { isLoggedIn } from "./auth";
import LoginForm from "./components/LoginForm";
import Chat from "./components/Chat";
import Logout from "./components/Logout";
import CharacterList from "./components/CharacterList";

function App() {
  const [selectedOption, setSelectedOption] = useState("Home");
  const [loggedIn, setLoggedIn] = useState(false);
  const onSelectOption = (option: string) => {
    setSelectedOption(option);
  };

  const onEvaluate = (option: number) => {
    setSelectedOption("Evaluate");
  };

  useEffect(() => {
    setLoggedIn(isLoggedIn());
  }, []);

  if (!loggedIn) {
    return (
      <div>
        <NavBar onSelectOption={onSelectOption}></NavBar>
        {selectedOption === "Home" && <HomePage></HomePage>}
        {selectedOption === "Login" && <LoginForm></LoginForm>}
      </div>
    );
  }

  return (
    <div>
      <NavBar onSelectOption={onSelectOption}></NavBar>
      {selectedOption === "Home" && <HomePage></HomePage>}
      {selectedOption === "Bookshelf" && (
        <Bookshelf onEvaluate={onEvaluate}></Bookshelf>
      )}
      {selectedOption === "Evaluate" && <Novel></Novel>}
      {selectedOption === "Characters" && <CharacterList></CharacterList>}
      {selectedOption === "Overview" && <Overview></Overview>}
      {selectedOption === "Chat" && <Chat></Chat>}
      {selectedOption === "Logout" && <Logout></Logout>}
    </div>
  );
}

export default App;
