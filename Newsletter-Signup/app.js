const express = require("express");
const request = require("request");
const app = express();
app.use(express.json());
app.use(express.urlencoded());
app.use(express.static('public'));

app.get("/", function(req,res){
    res.sendFile(__dirname+"/public/signup.html");
});

app.post("/", function(req,res){
    const firstName = req.body.firstName;
    const lastName = req.body.lastName;
    const email = req.body.email;
    res.write(firstName);
    res.write(lastName);
    res.write(email);
    res.send();
});


app.listen(3000, function(){
    console.log("Server is running.");
});