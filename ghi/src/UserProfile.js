import React, {useEffect, useState } from 'react';
import { useAuthContext } from "./Auth";

function ProfilePage() {
    const { token } = useAuthContext();
    const [username, setUsername] = useState([]);
    const fetchProfileData = async () => {
            const URL = `${process.env.REACT_APP_SWOOP_SERVICE_API_HOST}/api/accounts`;

            const response = await fetch(URL, {
                headers: { Authorization: `Bearer ${token}` },
            });

            if (response.ok) {
                const data = await response.json();
                setUsername(data)
            }
        }
    useEffect(() => {
        const fetchProfileData = async () => {
            const URL = `${process.env.REACT_APP_SWOOP_SERVICE_API_HOST}/api/accounts`;

            const response = await fetch(URL, {
                headers: { Authorization: `Bearer ${token}` },
            });

            if (response.ok) {
                const data = await response.json();
                setUsername(data)
            }
        }
        fetchProfileData();
    }, [token]);

  return (
    <>
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
    </div>
    </>
)};

export default ProfilePage
