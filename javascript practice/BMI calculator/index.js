const express = require("express");
const app = express();
app.use(express.json());
app.use(express.urlencoded({extended: true}));


app.get("/", function(req,res){
    res.sendFile(__dirname+"/index.html");
});

app.post("/", function(req,res){
    let weight = Number(req.body.bodyWeight);
    let cmHeight = Number(req.body.height);
    let height = cmHeight/100;
    let bmiIndex = Math.floor(weight/Math.sqrt(height));
    res.send("Your BMI index is " + bmiIndex)
})


app.listen(3000, function(){
    console.log("Server is running");
});
