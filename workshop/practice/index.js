const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const path = require("path");

app.use(express.static('public'))

app.listen(3000, function(){
    console.log("Server started on 3000 port.")
});