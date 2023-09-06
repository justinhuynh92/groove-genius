import { React, useEffect, useState } from "react";
import "../stylesheets/playlist-detail.css";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useParams } from "react-router-dom";

const PlaylistDetail = () => {
  const [playlist, setPlaylist] = useState({ tracks: [] });
  const { token } = useToken();
  const { id } = useParams();
  useEffect(() => {
    if (!token || !id) return;
    const fetchData = async () => {
      try {
        const response = await fetch(`http://localhost:8000/playlists/${id}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });

        const data = await response.json();

        if (response.ok) {
          setPlaylist(data);
        }
      } catch (err) {
        console.error("Caught an error: ", err);
      }
    };

    fetchData();
  }, [token, id]);

  return (
    <div className="playlist-container">
      <h1 className="playlist-header">{playlist.name}</h1>
      <ul className="playlist-tracks">
        {playlist.tracks.map((track, id) => (
          <li key={id} className="playlist-track">
            {track.title} - {track.artist}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlaylistDetail;
