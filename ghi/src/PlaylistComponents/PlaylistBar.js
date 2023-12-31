import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";
import "../stylesheets/playlist-bar.css";

const PlaylistBar = () => {
  const [playlists, setPlaylists] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isError, setIsError] = useState(false);
  const { token } = useToken();

  useEffect(() => {
    if (!token) return;

    const fetchData = async () => {
      try {
        setIsError(false);
        setIsLoading(true);
        const response = await fetch(
          "https://may-8-pt-groove-genius.mod3projects.com/playlists",
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          }
        );

        const data = await response.json();

        if (response.ok) {
          setPlaylists(data);
        } else {
          setIsError(true);
        }
      } catch (err) {
        setIsError(true);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [token]);

  return (
    <div className="playlist-bar-container">
      <h1 className="playlist-bar-header">Playlists</h1>
      {isLoading ? <div>Loading...</div> : null}
      {isError ? <div>Error loading playlists!</div> : null}
      <ul className="playlist-bar-list">
        {playlists.map((playlist, index) => (
          <li key={index} className="playlist-item">
            <Link to={`/playlists/${playlist.id}`}>{playlist.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlaylistBar;
