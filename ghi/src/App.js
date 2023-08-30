import { useState } from "react";
import Construct from "./Construct.js";
import ErrorNotification from "./ErrorNotification";
import "./App.css";
import LoginForm from "./LogInForm.js";
import SignupForm from "./SignUpForm.js";
import GenreList from "./genres/ListOfGenres.js";
import GenreForm from "./genres/CreateGenreForm.js";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";

function App() {
  // const domain = /https:\/\/[^/]+/;
  // const basename = process.env.PUBLIC_URL.replace(domain, "");

  return (
    <div>
      <BrowserRouter>
        <AuthProvider baseUrl={'http://localhost:8000'}>
          <Routes>
            <Route path="/login" element={<LoginForm />} />
            <Route path="/signup" element={<SignupForm />} />
            <Route path="/genres" element={<GenreList />} />
            <Route path="/genres/new" element={<GenreForm />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
