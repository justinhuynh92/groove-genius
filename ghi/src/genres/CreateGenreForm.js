import React, { useState } from "react";
import GenreList from "./ListOfGenres";

function GenreForm({}) {
  const [name, setName] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {};
    data.name = name;

    const genreUrl = "http://localhost:8000/genres/new";
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(genreUrl, fetchConfig);
    if (response.ok) {
      window.location.href = "http://localhost:3000/genres/new";
      setName("");
    }
  };
  function handleChangeName(event) {
    const { value } = event.target;
    setName(value);
  }
  return (
    <>
      <div className="container">
        <GenreList />
      </div>
      <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Create New Genre</h1>
            <form onSubmit={handleSubmit} id="create-genre-form">
              <div className="form-floating mb-3">
                <input
                  value={name}
                  onChange={handleChangeName}
                  placeholder="Genre Name"
                  required
                  type="text"
                  name="name"
                  id="name"
                  className="form-control"
                />
              </div>
              <button className="btn btn-primary">Create</button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}

export default GenreForm;
