import "./App.css";
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import user from "../src/img/user.png";
import register from "../src/img/register.png";
import logIn from "../src/img/login.png";
import genre from "../src/img/genre.png";
import playlist from "../src/img/playlist.jpg";
import tracks from "../src/img/tracks.jpg";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";

function DropDown() {
  const [open, setOpen] = useState(false);
  const { token, logout } = useToken();
  const navigate = useNavigate();

  const handleLogOut = () => {
    navigate(`/login`);
  };

  const LogUserOut = async () => {
    logout();
  };

  useEffect(() => {
    if (!token) return;
  }, [token]);

  return <>{token ? <LoggedInNav /> : <LoggedOutNav />}</>;

  function LoggedInNav() {
    return (
      <div className="App">
        <div className="menu-container">
          <div
            className="menu-trigger"
            onClick={() => {
              setOpen(!open);
            }}
          >
            <img src={user} alt="user pic"></img>
          </div>
          <div className={`dropdown-menu ${open ? "active" : "inactive"}`}>
            <h3>
              User
              <br />
              <span>Profile</span>
            </h3>
            <ul>
              <Link to="/profile">
                <DropdownItem img={user} text={"My Profile"} />
              </Link>
              <Link to="/genres/new">
                <DropdownItem img={genre} text={"Create Genre"} />
              </Link>
              <Link to="/playlists/new">
                <DropdownItem img={playlist} text={"Create Playlist"} />
              </Link>
              <Link to="/tracks">
                <DropdownItem img={tracks} text={"Create Track"} />
              </Link>
              <button
                onClick={() => {
                  LogUserOut();
                  handleLogOut();
                }}
              >
                Log Out
              </button>
            </ul>
          </div>
        </div>
      </div>
    );
  }

  function LoggedOutNav() {
    return (
      <div className="App">
        <div className="menu-container">
          <div
            className="menu-trigger"
            onClick={() => {
              setOpen(!open);
            }}
          >
            <img src={user} alt="user pic"></img>
          </div>
          <div className={`dropdown-menu ${open ? "active" : "inactive"}`}>
            <h3>
              User
              <br />
              <span>Profile</span>
            </h3>
            <ul>
              <Link to="/login">
                <DropdownItem img={logIn} text={"Log In"} />
              </Link>
              <Link to="/signup">
                <DropdownItem img={register} text={"Sign Up"} />
              </Link>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

function DropdownItem(props) {
  return (
    <li className="dropdownItem">
      <img src={props.img} alt="prop pic"></img>
      <p> {props.text} </p>
    </li>
  );
}

export default DropDown;
