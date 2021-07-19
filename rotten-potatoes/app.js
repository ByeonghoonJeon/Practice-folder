const express = require("express");
const app = express();

const exphbs = require("express-handlebars");

app.engine('handlebars', exphbs({ defaultLayout: 'main' }));
app.set('view engine', 'handlebars');

app.get ("/", function(req, res){
    res.render("home", {msg:"Handlebars are cool"});
});

app.listen(3000, function(){
    console.log("Server is working on port 3000");
});
