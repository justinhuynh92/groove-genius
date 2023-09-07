import React, {useEffect, useState} from 'react';
import useToken from "@galvanize-inc/jwtdown-for-react";

function ProfilePage() {
    const {token, logout, fetchWithToken} = useToken();
    const [username, setUsername] = useState('');

    const logUserOut = async () => {
        logout();
        setUsername([]);
    }
    const getUserData = async () => {
        if (token) {
            const url = `http://localhost:8000/accounts`
            const user = await fetchWithToken(url);
            setUsername(user.username);
        }
    }
    useEffect(() => {
        getUserData();
    }, [token]);

    return (
        <div className="p-4">
            <div className="mb-4">
                <h1 className="text-2xl font-bold">Hello, {username}</h1>
            </div>
            <div className="bg-white shadow-md rounded-lg p-4">
                <ul>
                    <li className="mb-2">
                        <h2 className="text-lg font-semibold">Username</h2>
                    </li>
                    <li className="list-group-item border bg-light">Genre</li>
                    <li className="list-group-item border bg-light">Tracks</li>
                    <li className="list-group-item border bg-light">Playlists</li>
                </ul>
            </div>
        </div>
        )
};

export default ProfilePage
