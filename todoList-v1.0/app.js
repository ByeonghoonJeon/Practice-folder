const express = require("express");
const bodyParser = require("body-parser");
const app = express();
var items=["Buy Food"];
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended:true}));
//when a user approaches to the home = app.get("/", fu...)

app.get("/", function(req, res){
    var today = new Date();
    
    var options = {
        weekday: "long",
        day: "numeric",
        month: "long"
    };

    var day = today.toLocaleDateString("en-US", options);
    
    res.render("list", {
        kindOfDay: day, newListItems: items
    });
});

app.post("/", function(req, res){
    var item = req.body.newItem
    items.push(item);
    console.log(item);
    res.redirect("/");
})

//show screen above.


// and listen via port xxxx 
app.listen(3000, function(){ 
    console.log("Server started on port 3000");
});