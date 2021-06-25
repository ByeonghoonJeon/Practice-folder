const express = require("express");
const https = require("https");
const app = express();

app.use(express.json());
app.use(express.urlencoded());
app.use(express.static('public'));

app.post("/", function(req,res){
    
    console.log(req.body.cityName);

    const query = req.body.cityName;
    const apiKey = "51fad77e11441b96834a30e61a4d1f50";
    const units = "metric";
    const url = "https://api.openweathermap.org/data/2.5/weather?q="+query+"&appid="+apiKey+"&units="+units;
   
    https.get(url, function(response){
        console.log(response.statusCode);
        
        response.on("data", function(data){
            const weatherData = JSON.parse(data);
            const fullTemp = weatherData.main.temp
            const temp = fullTemp.toFixed(1);
            const weatherDescription = weatherData.weather[0].description
            res.write("<p>Current weather of "+query+" is "+weatherDescription+".</p>");
            res.write("<h1>Today's temperature is: "+temp+" degree</h1>");
            res.send();
            
        });
    });
})

app.listen(3000, function(){
    console.log("Server is working");
});