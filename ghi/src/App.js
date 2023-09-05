import "./App.css";
import LoginForm from "./LogInForm.js";
import SignupForm from "./SignUpForm.js";
import GenreList from "./genres/ListOfGenres.js";
import GenreForm from "./genres/CreateGenreForm.js";
import PlaylistList from "./Components/PlaylistList";
import CreatePlaylist from "./Components/CreatePlaylist";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Nav from "./Nav.js";
import ProfilePage from "./UserProfile.js";

function App() {
  // const domain = /https:\/\/[^/]+/;
  // const basename = process.env.PUBLIC_URL.replace(domain, "");

  return (
    <div>
      <BrowserRouter>
        <Nav />
        <AuthProvider baseUrl={"http://localhost:8000"}>
          <Routes>
            <Route path="/login" element={<LoginForm />} />
            <Route path="/signup" element={<SignupForm />} />
            <Route path="/genres" element={<GenreList />} />
            <Route path="/genres/new" element={<GenreForm />} />
            <Route path="/playlists" element={<PlaylistList />} />
            <Route path="/playlists/new" element={<CreatePlaylist />} />
            <Route path="/profile" element={<ProfilePage />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
