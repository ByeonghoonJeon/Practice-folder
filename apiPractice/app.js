const express = require("express");
const { STATUS_CODES } = require("http");
const https = require("https");
const app = express();

app.get("/", function(req, res){

    const url = "https://api.openweathermap.org/data/2.5/weather?q=vienna&appid=51fad77e11441b96834a30e61a4d1f50&units=metric"
    https.get(url, function(response){
        console.log(response.statusCode);
        response.on("data",function(data){
            const weatherData = JSON.parse(data);
            const temperature = weatherData.main.temp;
            const temp = Math.floor(temperature);
            console.log(temp);
            const weatherDescription = weatherData.weather[0].description;
            const icon = weatherData.weather[0].icon;
            const imageURL = "http://openweathermap.org/img/wn/"+icon+"@2x.png"
            console.log(weatherDescription);
            res.write("<h1>The weather is currently "+ weatherDescription+"</h1>");
            res.write("<h1>The temperature in Vienna is "+temp+" degree celcius.</h1>");
            res.write("<img src=" + imageURL + ">");
            res.send()
        })
    });

})



app.listen(3000,function(){
    console.log("Server is running on port 3000");
})