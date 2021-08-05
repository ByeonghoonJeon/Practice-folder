import React from "react";
import contacts from "../contacts";

function Card(props) {
  return (
    <div className="card">
      <div className="top">
        <h2 className="name">{contacts.name}</h2>
        <img
          className="circle-img"
          src="https://pbs.twimg.com/profile_images/625247595825246208/X3XLea04_400x400.jpg"
          alt="avatar_img"
        />
      </div>
      <div className="bottom">
        <p className="info">{contacts.phone}</p>
        <p className="info">{contacts.email}</p>
      </div>
    </div>
  );
}

export default Card;
