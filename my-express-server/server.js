const { response } = require("express");
const express = require("express");
const app = express();
app.get("/", function(req, res){
    res.send("Hello, world!");
});

app.get("/contact", function(req,res){
    res.send("Contact page");
});

app.get("/about", function(req,res){
    res.send("About me");
});
app.listen(3000, function(){
    console.log("Server started on port 3000");
});