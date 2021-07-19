const express = require("express");
const app = express();

const exphbs = require("express-handlebars");

let reviews = [
    {title: "Great Review", movieTitle: "Batman II"},
    {title: "Awesome Movie", movieTitle: "Titanic"}
];

app.engine('handlebars', exphbs({ defaultLayout: 'main' }));
app.set('view engine', 'handlebars');

app.get ("/", function(req, res){
    res.render("reviews-index", {reviews:reviews});
});

app.get("/reviews", function(req, res){
    res.render("reviews-index", {reviews: reviews});
});


app.listen(3000, function(){
    console.log("Server is working on port 3000");
});
