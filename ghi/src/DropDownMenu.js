import "./App.css";
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import user from "../src/img/user.png";
import logoutpic from "../src/img/log-out.png";
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
            <img src={user}></img>
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
                <DropdownItem img={user} text={"Create Genre"} />
              </Link>
              <Link to="/playlists/new">
                <DropdownItem img={user} text={"Create Playlist"} />
              </Link>
              <Link to="/tracks">
                <DropdownItem img={user} text={"Create Track"} />
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
            <img src={user}></img>
          </div>
          <div className={`dropdown-menu ${open ? "active" : "inactive"}`}>
            <h3>
              User
              <br />
              <span>Profile</span>
            </h3>
            <ul>
              <Link to="/login">
                <DropdownItem img={user} text={"Log In"} />
              </Link>
              <Link to="/signup">
                <DropdownItem img={user} text={"Sign Up"} />
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
      <img src={props.img}></img>
      <a> {props.text} </a>
    </li>
  );
}

export default DropDown;
