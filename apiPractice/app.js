const express = require("express");
const https = require("https");
const app = express();

app.get("/", function(req, res){

    const url = "https://api.openweathermap.org/data/2.5/weather?q=vienna&appid=51fad77e11441b96834a30e61a4d1f50"
    https.get(url, function(response){
        console.log(response);
    });
    res.send("Server is up and running.");
})



app.listen(3000,function(){
    console.log("Server is running on port 3000");
})