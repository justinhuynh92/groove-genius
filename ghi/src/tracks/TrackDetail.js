import { useEffect, useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";

function TrackDetail() {
  const [tracks, setTracks] = useState([]);
  const [title, setTitle] = useState('');
  const {token, fetchWithToken} = useToken();
  const [notFound, setNotFound] = useState(false);
  const navigate = useNavigate();


  async function getTrack(title) {
    if(token){
    const response = await fetchWithToken(`http://localhost:8000/tracks?title=${title}`)
      if (response.length === undefined) {
          setNotFound(true);
        } else {
          setNotFound(false);
          setTracks(response)
    }
    
    } else {
      console.error("An error occured");
    }
  }


  async function handleDeleteTrack(id){
        const locationURL = `http://localhost:8000/tracks/${id}`
        const fetchConfig = {
            method: "DELETE"
        };
        const response = await fetch(locationURL, fetchConfig);
         if (response.ok) {
           setTracks((prevTracks) => {
            return prevTracks.filter((track) => track[0] !== id);
          });
        }
    }

  const handleTitleChange = (e) => {
    const value = e.target.value;
    setTitle(value);
  };

   const handleSubmit = (event) => {
    event.preventDefault(); 
    getTrack(title);
  };

   const handleTrackDetail = (id) => {
    navigate(`/tracks/${id}`);
  };

useEffect(() => {
    }, [token]);


  return (
    <div>
    <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter a track title"
          value={title}
          onChange={handleTitleChange}
        />
        <button type="submit">Submit</button>
      </form>
    {notFound ? (
        <h2>Track with title not found</h2>
      ) : (  
    <table className="table table-striped">
      <thead>
        <tr>
          <th>Title</th>
          <th>Artist</th>
          <th>Album</th>
        </tr>
      </thead>
      <tbody>
      {tracks.map((trackInfo, index) => (
        <tr key={index}>
          <td style={{ paddingLeft: '10px' }}>{trackInfo[1]}</td> 
          <td style={{ paddingLeft: '10px' }} >{trackInfo[2]}</td>
          <td style={{ paddingLeft: '10px' }} >{trackInfo[3]}</td>
          <td>
            <button onClick={() => handleDeleteTrack(trackInfo[0])} className="btn btn-success">Delete</button>
          </td>
          <td>
                <button onClick={() => handleTrackDetail(trackInfo[0])} className="btn btn-primary">Details</button>
          </td>
        </tr>
      ))}
    </tbody>
    </table>
     )}
    </div>
  );
}

export default TrackDetail;
