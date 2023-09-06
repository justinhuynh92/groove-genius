import { NavLink, Link } from "react-router-dom";

function Nav() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">
          Groove Genius
        </NavLink>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <div
              className="collapse navbar-collapse"
              id="navbarNavDarkDropdown"
            >
              <ul className="navbar-nav">
                <li className="nav-item dropdown">
                  <a
                    className="nav-link dropdown-toggle"
                    id="navbarDarkDropdownMenuLink"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Genres
                  </a>
                  <ul
                    className="dropdown-menu dropdown-menu-dark"
                    aria-labelledby="navbarDarkDropdownMenuLink"
                  >
                    <li>
                      <Link className="dropdown-item" to="/genres">
                        All Genres
                      </Link>
                    </li>
                    <li>
                      <Link className="dropdown-item" to="/genres/{id}">
                        Get Genre
                      </Link>
                    </li>
                    <li>
                      <Link className="dropdown-item" to="/genres/new">
                        Create Genre
                      </Link>
                    </li>
                    <li>
                      <Link
                        className="dropdown-item"
                        to="/api/genre/{genre_id}"
                      >
                        Delete Genre
                      </Link>
                    </li>
                    <li>
                      <Link className="dropdown-item" to="/genres/{id}">
                        Update Genre
                      </Link>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
            <div
              className="collapse navbar-collapse"
              id="navbarNavDarkDropdown"
            >
              <ul className="navbar-nav" style={{ color: "black" }}>
                <li className="nav-item dropdown">
                  <a
                    className="nav-link dropdown-toggle"
                    id="navbarDarkDropdownMenuLink"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Playlists
                  </a>
                  <ul
                    className="dropdown-menu dropdown-menu-dark"
                    aria-labelledby="navbarDarkDropdownMenuLink"
                  >
                    <li>
                      <Link className="dropdown-item" to="/playlists/new">
                        Create Playlist
                      </Link>
                    </li>
                    <li>
                      <Link className="dropdown-item" to="/playlists">
                        All Playlists
                      </Link>
                    </li>
                    <li>
                      <Link
                        className="dropdown-item"
                        to="/playlists/{playlist_id}"
                      >
                        Get Playlist
                      </Link>
                    </li>
                    <li>
                      <Link
                        className="dropdown-item"
                        to="/playlists/{playlist_id}"
                      >
                        Update Playlist
                      </Link>
                    </li>
                    <li>
                      <Link
                        className="dropdown-item"
                        to="/playlists/{playlist_id}"
                      >
                        Delete Playlist
                      </Link>
                    </li>
                    <li>
                      <Link
                        className="dropdown-item"
                        to="/playlists/{playlist_id}/tracks/{track_id}"
                      >
                        Delete Playlist/Track
                      </Link>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
            <div
              className="collapse navbar-collapse"
              id="navbarNavDarkDropdown"
            >
              <ul className="navbar-nav" style={{ color: "black" }}>
                <li className="nav-item dropdown">
                  <a
                    className="nav-link dropdown-toggle"
                    id="navbarDarkDropdownMenuLink"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Tracks
                  </a>
                  <ul
                    className="dropdown-menu dropdown-menu-dark"
                    aria-labelledby="navbarDarkDropdownMenuLink"
                  >
                    <li>
                      <Link className="dropdown-item" to="/tracks/new">
                        Create Track
                      </Link>
                    </li>
                    <li>
                      <Link className="dropdown-item" to="/tracks">
                        Get Track
                      </Link>
                    </li>
                    <li>
                      <Link className="dropdown-item" to="/tracks/{track_id}">
                        Delete Track
                      </Link>
                    </li>
                    <li>
                      <Link className="dropdown-item" to="/tracks/{track_id}">
                        Update Track
                      </Link>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Nav;
