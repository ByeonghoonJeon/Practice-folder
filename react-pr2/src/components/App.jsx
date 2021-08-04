import React from "react";
import Contacts from "contacts";
function App(props) {
  return (
    <div>
      <h1 className="heading">My Contacts</h1>
      <div className="card">
        <div className="top">
          <h2 className="name">{Contacts.name}</h2>
          <img className="circle-img" src={Contacts.imgURL} alt="avatar_img" />
        </div>
        <div className="bottom">
          <p className="info">{Contacts.phone}</p>
          <p className="info">{Contacts.email}</p>
        </div>
      </div>
    </div>
  );
}

export default App;
