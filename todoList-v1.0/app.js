const express = require("express");
const bodyParser = require("body-parser");
const app = express();


//when a user approaches to the home = app.get("/", fu...)
app.get("/", function(req, res){
    var today = new Date();
    var currentDay = today.getDay();
    if (currentDay === 6 || currentDay=== 0){
        res.write("<h1>Yay it's weekend</h1>");
    }
    else{
        res.sendFile(__dirname+"/index.html");
    }
//getDay = gives number values according to the day (Sun =0 Mon=1 Tue =2...)
});


//show screen above.


// and listen via port xxxx 
app.listen(1992, function(){ 
    console.log("Server started on port 1992");
});