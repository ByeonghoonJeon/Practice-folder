const express = require("express");
const app = express();

app.set('view engine', "ejs");

app.use(express.json());
app.use(express.urlencoded());

app.get("/", function(req,res){
    var today = new Date();
    var currentDay = today.getDay();
    if (currentDay===6 || currentDay===0){
        res.sendFile(__dirname+ "/weekdays.html");
    }else{
        res.sendFile(__dirname+ "/weekend.html");
    }
});

app.listen(3000, function(){
    console.log("Server is running.")
})