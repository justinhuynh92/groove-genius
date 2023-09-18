import "./App.css";
import LoginForm from "./LogInForm.js";
import SignupForm from "./SignUpForm.js";
import GenreList from "./genres/ListOfGenres.js";
import GenreForm from "./genres/CreateGenreForm.js";
import PlaylistList from "./Components/PlaylistList";
import CreatePlaylist from "./Components/CreatePlaylist";
import PlaylistDetail from "./Components/PlaylistDetail";
import TrackDetail from "./tracks/TrackDetail";
import TrackDetailView from "./tracks/TrackDetailView";
import TrackForm from "./tracks/CreateTrackForm";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Banner from "./Components/Banner.js";
import ProfilePage from "./UserProfile.js";
import PlayerPage from "./Components/PlayerPage";
import PlaylistBar from "./Components/PlaylistBar";

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");

  return (
    <div className="center-wrapper">
      <div className="main-container">
        <BrowserRouter basename={basename}>
          <AuthProvider
            baseUrl={"https://may-8-pt-groove-genius.mod3projects.com"}
          >
            <Banner />
            <PlaylistBar />
            <Routes>
              <Route path="/" element={<PlayerPage />} />
              <Route path="/login" element={<LoginForm />} />
              <Route path="/signup" element={<SignupForm />} />
              <Route path="/genres" element={<GenreList />} />
              <Route path="/genres/new" element={<GenreForm />} />
              <Route path="/playlists" element={<PlaylistList />} />
              <Route path="/playlists/new" element={<CreatePlaylist />} />
              <Route path="/playlists/:id" element={<PlaylistDetail />} />
              <Route path="/tracks" element={<TrackDetail />} />
              <Route path="/tracks/:id" element={<TrackDetailView />} />
              <Route path="/tracks/new" element={<TrackForm />} />
              <Route path="/profile" element={<ProfilePage />} />
            </Routes>
          </AuthProvider>
        </BrowserRouter>
      </div>
    </div>
  );
}

export default App;
