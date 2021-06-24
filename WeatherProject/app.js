const express = require("express");
const { Http2ServerResponse } = require("http2");
const https = require("https");

const app = express();

app.get("/", function(req,res){
    const url = "https://api.openweathermap.org/data/2.5/weather?q=Vienna&appid=51fad77e11441b96834a30e61a4d1f50&units=metric";
   
    https.get(url, function(response){
        console.log(response.statusCode);
        
        response.on("data", function(data){
            const weatherData = JSON.parse(data);
            const temp = weatherData.main.temp
            const weatherDescription = weatherData.weather[0].description
            res.write("<h1>Current weather is "+weatherDescription+".</h1>")
            res.write("<h1>Today's temperature is: "+temp+" degree</h1>");
            
        });
    });
})

app.listen(3000, function(){
    console.log("Server is working");
});