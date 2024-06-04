import React from "react";

const Logout: React.FC = () => {
  const handleLogout = () => {
    localStorage.removeItem("token");
    // Redirect to login page
    window.location.href = "/login";
  };

  return (
    <div className="container">
      <br></br>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Logout;
