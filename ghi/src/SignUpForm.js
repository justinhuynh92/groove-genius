import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function SignupForm() {
  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();
  const handleUserNameChange = (e) => {
    const value = e.target.value;
    setUserName(value);
  };
  const handlePasswordChange = (e) => {
    const value = e.target.value;
    setPassword(value);
  };
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {};
    data.username = username;
    data.password = password;
    const userUrl = `http://localhost:8000/users`;
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(userUrl, fetchConfig);
    if (response.ok) {
      setUserName("");
      setPassword("");
      navigate("/login");
    }
  };

  return (
    <div>
      <div>
        <form onSubmit={handleSubmit}>
          <h1>Sign Up!</h1>
          <div>
            <input
              type="text"
              value={username}
              onChange={handleUserNameChange}
            />
            <label>Username:</label>
            <br />
          </div>
          <div>
            <input
              type="password"
              value={password}
              onChange={handlePasswordChange}
            />
            <label>Password:</label>
            <br />
          </div>
          <button type="submit">Sign Up!</button>
        </form>
      </div>
    </div>
  );
}

export default SignupForm;
