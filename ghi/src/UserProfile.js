import React, {useEffect, useState} from 'react';
import useToken from "@galvanize-inc/jwtdown-for-react";

function ProfilePage() {
    const {token, logout, fetchWithToken} = useToken();
    const [username, setUsername] = useState([]);

    const logUserOut = async () => {
        logout();
        setUsername([]);
    }
    const getUserData = async () => {
        if (token) {
            const url = `http://localhost:8000/profile/`
            const user = await fetchWithToken(url);
            setUsername(user);
        }
    }
    useEffect(() => {
        getUserData();
    }, [token]);

    return (
        <div>
            <div>
                <h1>Hello, {username}</h1>
            </div>
            <div>
            <ul>
                <li>
                    <h2>Username</h2>
                    <p>{username}</p>
                </li>
            </ul>
            </div>
            <div>
            <button onClick={logUserOut}>Logout</button>
            </div>
        </div>
    )
};

export default ProfilePage
