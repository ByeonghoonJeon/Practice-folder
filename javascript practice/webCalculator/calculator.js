const express = require("express");
const app = express();
app.use(express.json());
app.use(express.urlencoded({extended: true}));


app.get("/", function(req,res){
    res.sendFile(__dirname+"/index.html");
});

app.post("/", function(req,res){

var number1 = Number(req.body.num1);
var number2 = Number(req.body.num2);
var result = number1 + number2; 
    res.send(`${result}`);
});


app.listen(3000, function(){
    console.log("Server is working");
});