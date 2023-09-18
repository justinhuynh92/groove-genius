import React, { useEffect, useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { Link } from "react-router-dom";
import "./stylesheets/profile-page.css";

function ProfilePage() {
  const { token, fetchWithToken } = useToken();
  const [username, setUsername] = useState("");

  useEffect(() => {
    const getUserData = async () => {
      if (token) {
        const url = `https://may-8-pt-groove-genius.mod3projects.com/accounts`;
        const user = await fetchWithToken(url);
        setUsername(user.username);
      }
    };
    getUserData();
  }, [token, fetchWithToken]);

  return (
    <div className="profile-container">
      <div className="header-section">
        <h1 className="greeting-text">Hello, {username}</h1>
      </div>
      <div className="library-section">
        <ul className="library-list">
          <li className="library-item">
            <h2 className="section-title">My Library</h2>
          </li>
          <li className="list-link">
            <Link to="/genres">Genre</Link>
          </li>
          <li className="list-link">
            <Link to="/tracks">Tracks</Link>
          </li>
          <li className="list-link">
            <Link to="/playlists">Playlists</Link>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default ProfilePage;
