const express = require("express");
const app = express();

app.get("/", function(req,res){
    res.send("Hello new");
});

app.listen(3000, function(){
    console.log("Server is working");
});