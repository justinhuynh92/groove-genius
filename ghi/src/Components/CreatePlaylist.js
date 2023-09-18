import React, { useState, useEffect } from "react";
import "../stylesheets/create-playlist.css";
import useToken from "@galvanize-inc/jwtdown-for-react";

const CreatePlaylist = () => {
  const [name, setName] = useState("");
  const [playlistCreated, setPlaylistCreated] = useState(false);
  const { token } = useToken();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(
        "https://may-8-pt-groove-genius.mod3projects.com/playlists",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({ name }),
        }
      );

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
    if (!token) return;
    if (playlistCreated) {
      setTimeout(() => {
        setPlaylistCreated(false);
        window.location.reload();
      }, 3000);
    }
  }, [playlistCreated, token]);
  return (
    <div className="main-container">
      <div className="main-content">
        <h1>Create a Playlist</h1>
        {playlistCreated ? (
          <p>Playlist created! Lit, like a fire jutsu!</p>
        ) : (
          <>
            <form onSubmit={handleSubmit}>
              <label htmlFor="playlist-name">Playlist Name:</label>
              <input
                type="text"
                id="playlist-name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter your fire playlist name here"
                required
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
