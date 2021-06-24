const express = require("express");
const https = require("https");

const app = express();

app.get("/", function(req,res){
    res.sendFile(__dirname+"/index.html");
})
//     const query = "Vienna";
//     const apiKey = "51fad77e11441b96834a30e61a4d1f50";
//     const units = "metric";
//     const url = "https://api.openweathermap.org/data/2.5/weather?q="+query+"&appid="+apiKey+"&units="+units;
   
//     https.get(url, function(response){
//         console.log(response.statusCode);
        
//         response.on("data", function(data){
//             const weatherData = JSON.parse(data);
//             const temp = weatherData.main.temp
//             const weatherDescription = weatherData.weather[0].description
//             res.write("<p>Current weather of "+query+" is "+weatherDescription+".</p>");
//             res.write("<h1>Today's temperature is: "+temp+" degree</h1>");
//             res.send();
            
//         });
//     });
// })

// app.listen(3000, function(){
//     console.log("Server is working");
// });