const express = require("express");
const app = express ();
app.use(express.json()); //Used to parse JSON bodies
app.use(express.urlencoded()); //Parse URL-encoded bodies

app.get("/", function(req, res){
    res.send("hello");
});

app.listen(3000, function(){
    console.log("Server is running");
});