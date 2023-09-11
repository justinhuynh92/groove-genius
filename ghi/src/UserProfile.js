import React, { useEffect, useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { Link } from "react-router-dom";

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
        <div className="p-4">
            <div className="mb-4">
                <h1 className="text-2xl font-bold">Hello, {username}</h1>
            </div>
            <div className="bg-white shadow-md rounded-lg p-4">
                <ul>
                    <li className="mb-2">
                        <h2 className="text-lg font-semibold">My Library</h2>
                    </li>
                    <li className="list-group-item border bg-light">
                        <Link to="/genres">Genre</Link>
                    </li>
                    <li className="list-group-item border bg-light">
                        <Link to="/tracks">Tracks</Link>
                    </li>
                    <li className="list-group-item border bg-light">
                        <Link to="/playlists">Playlists</Link>
                    </li>
                </ul>
            </div>
        </div>
    )
};

export default ProfilePage;
