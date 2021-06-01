const express = require("express");
const bodyParser = require("body-parser");
const app = express();


//when a user approaches to the home = app.get("/", fu...)
app.get("/", function(req, res){
    var today = new Date();
    if (today.getDay()=== 6 || today.getDay()===0){
        res.send("Yay it's the weekend!");
    }
    else{
        res.send("Boo! I have to work");
    }
//getDay = gives number values according to the day (Sun =0 Mon=1 Tue =2...)
});


//show screen above.


// and listen via port xxxx 
app.listen(1992, function(){ 
    console.log("Server started on port 1992");
});