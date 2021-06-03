const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const path = require("path");
let items=["Buy Food"];
let workItems = [];
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static('public'))
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
        listTitle: day, newListItems: items
    });
});

app.post("/", function(req, res){
    var item = req.body.newItem
    items.push(item);
    console.log(item);
    res.redirect("/");
})

//show screen above.


app.get("/work", function(req,res){
    res.render("list", {listTitle:"Work List", newListItems: workLItems});
});

app.post("/work", function(req,res){
    let item = req.body.newItem;
    res.redirect
})

// and listen via port xxxx 
app.listen(3000, function(){ 
    console.log("Server started on port 3000");
});