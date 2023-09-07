import React, { useState, useEffect } from "react";
import "../stylesheets/playlist-list.css";
import useToken from "@galvanize-inc/jwtdown-for-react";

const PlaylistList = () => {
  const [playlists, setPlaylists] = useState([]);
  const { token } = useToken();

  // Use useEffect to fetch data when component mounts
  useEffect(() => {
    if (!token) return;
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/playlists", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });

        const data = await response.json();

        if (response.ok) {
          setPlaylists(data);
        }
      } catch (err) {
        console.error("Caught an error: ", err);
      }
    };

    fetchData();
  }, [token]);

  return (
    <div className="playlist-container">
      <h1 className="playlist-header">Playlists</h1>
      <ul className="playlist-list">
        {playlists.map((playlist, index) => (
          <li key={index} className="playlist-item">
            {playlist.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlaylistList;
