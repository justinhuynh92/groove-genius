import { useState, useEffect } from "react";

function GenreList() {
  const [genre, setGenre] = useState([]);
  async function getGenre() {
    const response = await fetch("http://localhost:8000/genres")
;
    if (response.ok) {
      const data = await response.json();
      setGenre(data);
    } else {
      console.error("An error occured");
    }
  }

  useEffect(() => {
    getGenre();
  }, []);

  return (
    <table className="table table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        {genre.map((genre) => {
          return (
            <tr key={genre.id}>
              <td>{genre.id}</td>
              <td>{genre.name}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default GenreList;
