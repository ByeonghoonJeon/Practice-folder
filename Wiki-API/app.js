//jshint esversion:6

const express = require("express");
const ejs = require("ejs");
const mongoose = require('mongoose');
const app = express();
app.use(express.json()); //Used to parse JSON bodies
app.use(express.urlencoded()); //Parse URL-encoded bodies
app.set('view engine', 'ejs');
app.use(express.static("public"));


mongoose.connect("mongodb://localhost:27017/wikiDB", {useNewUrlParser: true});
const articleSchema = {
  title: String,
  contents: String
};

const Article = mongoose.model("Article", articleSchema);

//TODO

app.listen(3000, function() {
  console.log("Server started on port 3000");
});