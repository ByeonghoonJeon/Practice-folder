const express = require("express"); // it is a loading of Express Package.
const app = express(); // it is how i creat express application.



app.get("/", (req, resp) => {
  resp.status(400).json({ message: "OK it works" });
});

app.get("/login", (req, resp) => {
  resp.json({
    message: "welcome",
  });
});
app.listen(3000, () => {
  console.log("It works");
});
