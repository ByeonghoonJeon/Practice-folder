const express = require("express");
const bodyParser = require("body-parser");
const app = express();

app.get("/", function(req, res){
    res.send("Hello");
});

app.listen(1992, function(){
    console.log("Server started on port 1992");
});