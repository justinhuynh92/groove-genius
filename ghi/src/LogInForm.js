import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";
const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [checker, setChecker] = useState(false);
  const [invalid, setInvalid] = useState(false);
const { login } = useToken();
  const handleInvalid = () => {
    setInvalid(true);
  };
  const handleChecker = () => {
    setChecker(!checker);
  };
  const fetchUser = async () => {
    const url = `${baseURL}/token`;
    const response = await fetch(url, {
      method: "GET",
      credentials: "include",
    });
    if (response.ok) {
      const data = await response.json();
      if (data === null) {
        handleInvalid();
      } else {
        navigate("/");
      }
    }
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(username, password);
    fetchUser();
  };
  useEffect(() => {
    login(username, password);
  }, [checker, login, username, password]);
