import { useEffect, useState} from "react";
import { useParams } from 'react-router-dom';
import useToken from "@galvanize-inc/jwtdown-for-react";

function TrackDetailView() {
    const [track, setTrack] = useState([]);
    const { id } = useParams();
    const {token, fetchWithToken} = useToken();


  async function getTrack() {
    if(token){
    const response = await fetchWithToken(`http://localhost:8000/tracks/${id}`)
        setTrack(response)
        console.log(response.genre_names)
    
    } else {
      console.error("An error occured");
    }
  }

useEffect(() => {
    getTrack()
    }, [token]);


  return (
    <div>
    <table className="table table-striped">
     <tbody>
        <tr>
        <td> 
            <h3>Title</h3>
        </td>
        <td>{track.title}</td>
        </tr>
        <tr>
        <td> 
            <h3>Artist</h3>
        </td>
        <td>{track.artist}</td>
        </tr>
        <tr>
        <td> 
            <h3>Album</h3>
        </td>
        <td>{track.album}</td>
        </tr>
        <tr>
        <td> 
            <h3>Genre(s)</h3>
        </td>
         <td>{track.genre_names}</td>
        </tr>
    </tbody>
    </table>
    </div>
  );
}

export default TrackDetailView;
