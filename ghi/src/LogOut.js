import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";

function LogOut() {
  const { logout } = useToken();
  const navigate = useNavigate();

  async function handleLogout(event) {
    logout();
    navigate("/login");
  }

  return (
    <div>
      <h1>Log Out</h1>
      <button onClick={handleLogout}>Log Out</button>
    </div>
  );
}
export default LogOut;
