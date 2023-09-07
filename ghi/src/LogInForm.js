import React, { useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";

function LoginForm() {
  const { login } = useToken();
  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");

  const handleUserNameChange = (e) => {
    const value = e.target.value;
    setUserName(value);
  };

  const handlePasswordChange = (e) => {
    const value = e.target.value;
    setPassword(value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(username, password);
  };

  return (
    <div>
      <div>
        <form onSubmit={handleSubmit}>
          <h1>Log In</h1>
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
          <button type="submit">Log In</button>
        </form>
      </div>
    </div>
  );
}

export default LoginForm;
