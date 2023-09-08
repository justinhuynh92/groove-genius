import { useState, useEffect } from "react";

function GenreList() {
  const [genre, setGenre] = useState([]);

  async function getGenre() {
    const response = await fetch(
      "https://may-8-pt-groove-genius.mod3projects.com/genres"
    );
    if (response.ok) {
      const data = await response.json();
      setGenre(data);
    } else {
      console.error("An error occured");
    }
  }

  async function handleDelete(genre) {
    const url = `https://may-8-pt-groove-genius.mod3projects.com/genres/${genre}`;
    const fetchConfig = {
      method: "DELETE",
    };
    const response = await fetch(url, fetchConfig);
    if (response.ok) {
      getGenre();
    }
  }

  useEffect(() => {
    getGenre();
  }, []);

  return (
    <table className="table table-striped">
      <thead>
        <tr>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        {genre.map((genre) => {
          return (
            <tr key={genre.id}>
              <td>{genre.name}</td>
              <td>
                <button onClick={() => handleDelete(genre.id)}>Delete</button>
              </td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default GenreList;
