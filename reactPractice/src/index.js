import React from "react";
import ReactDOM from "react-dom";

const today = new Date();
const currentTime = today.getHours();
let greeting = "";

const colorVariation = { color: "" };

if (currentTime < 12) {
  greeting = "Good monrning";
  colorVariation.color = "Green";
} else if (currentTime > 17) {
  greeting = "Good evening";
  colorVariation.cloor = "red";
} else {
  greeting = "Good afternoon";
  colorVariation.color = "pink";
}

ReactDOM.render(
  <h1 className="heading" style={colorVariation}>
    {greeting}
  </h1>,
  document.getElementById("root")
);