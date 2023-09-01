import React, { useState, useEffect } from "react";
import PlaylistBar from "./PlaylistBar.js";
import "../stylesheets/create-playlist.css";

const CreatePlaylist = () => {
  const [name, setName] = useState("");
  const [playlistCreated, setPlaylistCreated] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/playlists", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name }),
      });

      const data = await response.json();
      console.log(data);

      if (response.ok) {
        console.log("Playlist created: ", data);
        setPlaylistCreated(true);
      } else {
        console.error("Playlist not created: instead returned ", data);
      }
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    if (playlistCreated) {
      setTimeout(() => {
        setPlaylistCreated(false);
        window.location.reload();
      }, 3000);
    }
  }, [playlistCreated]);
  return (
    <div className="main-container">
      <PlaylistBar />
      <div className="main-content">
        <h1>Create a Playlist</h1>
        {playlistCreated ? (
          <p>Playlist created!</p>
        ) : (
          <>
            <form onSubmit={handleSubmit}>
              <label htmlFor="playlist-name">Playlist Name:</label>
              <input
                type="text"
                id="playlist-name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
              <button type="submit">Create Playlist</button>
            </form>
          </>
        )}
      </div>
    </div>
  );
};

export default CreatePlaylist;
