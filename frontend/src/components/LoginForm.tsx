import React, { useState, FormEvent, ChangeEvent } from "react";
import axios from "axios";

const LoginForm: React.FC = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [error, setError] = useState<string>("");

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();

    try {
      const response = await axios.post<{ token: string }>(
        "http://127.0.0.1:8000/api-token-auth/",
        {
          username,
          password,
        },
      );

      localStorage.setItem("token", response.data.token);
      window.location.href = "/home";
    } catch (error) {
      setError("Invalid username or password");
    }
  };

  const handleInputChange =
    (setState: React.Dispatch<React.SetStateAction<string>>) =>
    (event: ChangeEvent<HTMLInputElement>) =>
      setState(event.target.value);

  return (
    <div className="container">
      <form onSubmit={handleSubmit}>
        <h2>Login</h2>
        {error && <p>{error}</p>}
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={handleInputChange(setUsername)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={handleInputChange(setPassword)}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginForm;
