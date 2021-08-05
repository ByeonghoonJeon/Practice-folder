import React from "react";
import Card from "./Card";

function App(props) {
  return (
    <div>
      <h1 className="heading">My Contacts</h1>
      <Card name="Card.name" />
      <img src="Card.imgURL" />
      <Card phone="Card.phone" />
      <Card email="Card.email" />
    </div>
  );
}

export default App;
