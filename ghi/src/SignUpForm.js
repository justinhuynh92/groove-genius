import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";
function Signup() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();
  const handleNameChange = (e) => {
    const value = e.target.value;
    setName(value);
  };
  const handleEmailChange = (e) => {
    const value = e.target.value;
    setEmail(value);
  };
  const handlePasswordChange = (e) => {
    const value = e.target.value;
    setPassword(value);
  };
  const toggleShowPassword = () => {
    setShowPassword(!showPassword);
  };
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {};
    data.name = name;
    data.email = email;
    data.password = password;
    const userUrl = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users`;
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(userUrl, fetchConfig);
    if (response.ok) {
      setName("");
      setEmail("");
      setPassword("");
      navigate("/login");
    }
  };
