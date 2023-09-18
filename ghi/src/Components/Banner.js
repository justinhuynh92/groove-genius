import React from "react";
import "../stylesheets/banner.css"; // Import your CSS file if you're using one
import DropDown from "../DropDownMenu"; // Import the component you want to the right

const Banner = () => {
  return (
    <div className="banner-container">
      <div className="dropdown">
        <DropDown />
      </div>
    </div>
  );
};

export default Banner;
