const express = require("express");
const bodyParser = require("body-parser");
const app = express();
app.set('view engine', 'ejs');


//when a user approaches to the home = app.get("/", fu...)

app.get("/", function(req, res){
    var today = new Date();
    var currentDay = today.getDay();
    var day = "";

    if (currentDay === 6 || currentDay=== 0){
        day = "weekend";
        res.render("list", {
            kindOfDay: day
        });
    }
    else{
        day = "weekday";
        res.render("list", {
            kindOfDay: day
        });
    }
//getDay = gives number values according to the day (Sun =0 Mon=1 Tue =2...)
});


//show screen above.


// and listen via port xxxx 
app.listen(1992, function(){ 
    console.log("Server started on port 1992");
});