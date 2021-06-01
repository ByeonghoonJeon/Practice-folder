const express = require("express");
const bodyParser = require("body-parser");
const app = express();
app.set('view engine', 'ejs');

//when a user approaches to the home = app.get("/", fu...)

app.get("/", function(req, res){
    var today = new Date();
    var currentDay = today.getDay();
    var day = "";
    console.log(currentDay);

    if (currentDay === 0){
        day = "Sunday";
        res.render("list", {
            kindOfDay: day
        });
    }
    else if(currentDay===1){
        day = "Monday";
        res.render("list", {
            kindOfDay: day
        });
    }
    else if(currentDay===2){
        day = "Tuesday";
        res.render("list", {
            kindOfDay: day
        });
    }
    else if(currentDay===3){
        day = "Wednesday";
        res.render("list", {
            kindOfDay: day
        });
    }
    else if(currentDay===4){
        day = "Thursday";
        res.render("list", {
            kindOfDay: day
        });
    }
    else if(currentDay===5){
        day = "Friday";
        res.render("list", {
            kindOfDay: day
        });
    }
    else if(currentDay===6){
        day = "Saturday";
        res.render("list", {
            kindOfDay: day
        });
    }
//getDay = gives number values according to the day (Sun =0 Mon=1 Tue =2...)
});



//show screen above.


// and listen via port xxxx 
app.listen(3000, function(){ 
    console.log("Server started on port 3000");
});