import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";

function TrackDetailView() {
  const [track, setTrack] = useState([]);
  const { id } = useParams();
  const { token, fetchWithToken } = useToken();

  useEffect(() => {
  async function getTrack() {
    if (token) {
      try {
        const response = await fetchWithToken(
          `https://may-8-pt-groove-genius.mod3projects.com/tracks/${id}`
        );
        setTrack(response);
      } catch (error) {
        console.error("An error occurred:", error);
      }
    }
  }

    getTrack();
}, [token, id, fetchWithToken]);
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
            <td>{track.genre}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default TrackDetailView;
