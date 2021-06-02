const express = require("express");
const bodyParser = require("body-parser");
const app = express();

app.get("/", function(req, res){
    res.sendFile(__dirname+"/aboutus.html");
    
})

app.listen(3000, function(){
    console.log("Server started on 3000 port.")
})