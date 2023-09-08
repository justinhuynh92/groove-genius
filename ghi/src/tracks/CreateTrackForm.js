import React, { useState } from "react";

function TrackForm() {
  const [name, setName] = useState("");
  const [artist, setArtist] = useState("");
  const [album, setAlbum] = useState("");
  const [genres, setGenres] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {};
    data.title = name;
    data.artist = artist;
    data.album = album;
    data.genre_id = [genres];

    const trackUrl = "https://may-8-pt-groove-genius.mod3projects.com/tracks";
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(trackUrl, fetchConfig);
    if (response.ok) {
      setName("");
      setArtist("");
      setAlbum("");
      setGenres("");
    }
  };
  function handleChangeName(event) {
    const { value } = event.target;
    setName(value);
  }

  function handleChangeArtist(event) {
    const { value } = event.target;
    setArtist(value);
  }

  function handleChangeAlbum(event) {
    const { value } = event.target;
    setAlbum(value);
  }

  function handleChangeGenres(event) {
    const { value } = event.target;
    setGenres(value);
  }

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Create New Track</h1>
          <form onSubmit={handleSubmit} id="create-track-form">
            <div className="form-floating mb-3">
              <input
                value={name}
                onChange={handleChangeName}
                placeholder="Track Name"
                required
                type="text"
                name="name"
                id="name"
                className="form-control"
              />
              <input
                value={artist}
                onChange={handleChangeArtist}
                placeholder="Track Artist"
                required
                type="text"
                name="artist"
                id="artist"
                className="form-control"
              />
              <input
                value={album}
                onChange={handleChangeAlbum}
                placeholder="Track Album"
                required
                type="text"
                name="album"
                id="album"
                className="form-control"
              />
              <input
                value={genres}
                onChange={handleChangeGenres}
                placeholder="Track Genres"
                required
                type="num"
                name="genres"
                id="genres"
                className="form-control"
              />
            </div>
            <button className="btn btn-primary">Create</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default TrackForm;
