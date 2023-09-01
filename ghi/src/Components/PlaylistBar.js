import React, { useState, useEffect } from "react";
import "../stylesheets/playlist-bar.css";

const PlaylistBar = () => {
  const [playlists, setPlaylists] = useState([]);

  // Use useEffect to fetch data when component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/playlists", {
          method: "GET",
          headers: { "Content-Type": "application/json" },
        });

        const data = await response.json();

        if (response.ok) {
          setPlaylists(data);
        } else {
          console.error("Oops! Something went wrong, got ", data);
        }
      } catch (err) {
        console.error("Caught an exception: ", err);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="playlist-bar-container">
      <h1 className="playlist-bar-header">Playlists</h1>
      <ul className="playlist-bar-list">
        {playlists.map((playlist, index) => (
          <li key={index} className="playlist-item">
            {playlist.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlaylistBar;
