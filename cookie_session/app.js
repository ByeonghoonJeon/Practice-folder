//jshint esversion:6
require("dotenv").config();
const ejs = require("ejs");
const express = require("express");
const app = express();
const mongoose = require("mongoose");


app.use(express.json()); //Used to parse JSON bodies
app.use(express.urlencoded()); //Parse URL-encoded bodies
app.use(express.static("public"));
app.set("view engine", "ejs");

mongoose.connect("mongodb://localhost:27017/userDB", { useNewUrlParser: true });

const userSchema = new mongoose.Schema({
  email: String,
  password: String,
});

const User = new mongoose.model("User", userSchema);

app.get("/", function (req, res) {
  res.render("home");
});

app.get("/login", function (req, res) {
  res.render("login");
});

app.get("/register", function (req, res) {
  res.render("register");
});

app.post("/register", function (req, res) {
  
});

app.post("/login", function (req, res) {
  
});

app.listen(3000, function () {
  console.log("Server is running on port 3000");
});
