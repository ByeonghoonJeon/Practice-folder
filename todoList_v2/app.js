//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const date = require(__dirname + "/date.js");
const mongoose = require("mongoose");

const app = express();

app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

mongoose.connect("mongodb://localhost:27017/todolistDB", {
  useNewUrlParser: true,
});

const itemsSchema = new mongoose.Schema({
  name: String,
});

const Item = mongoose.model("item", itemsSchema);
const item1 = new Item({
  name: "welcome1",
});
const item2 = new Item({
  name: "welcome2",
});
const item3 = new Item({
  name: "welcome3",
});

const defaultItems = [item1, item2, item3];

const listSchema = {
  name: String,
  items: [itemsSchema]
};

const List = mongoose.model("List", listSchema);

app.get("/", function (req, res) {
  Item.find({}, function (err, foundItems) {
    if (foundItems.length === 0) {
      Item.insertMany(defaultItems, function(err){
        if (err) {
          console.log(err);
        } else {
          console.log("Succesfully added to database.");
        }
      });
      res.redirect("/");
    } else {
      res.render("list", { listTitle: "Today", newListItems: foundItems });
    }
  });
});

app.get("/:customListName", function(req, res){
  const customListName=req.params.customListName;

  List.findOne({name: customListName}, function(err, foundList){
    if (!err){
      if(!foundList){
        const list = new List({
          name: customListName,
          items: defaultItems
        });
          list.save();
      }else{
        res.render("list", { listTitle: foundList.name, newListItems: foundList.items})
      }
    }
  });

  
});

app.post("/", function (req, res) {
  const itemName = req.body.newItem;
  const item = new Item({
    name: itemName,
  });
  item.save();
  res.redirect("/");
});

app.post("/delete", function(req, res){
  const checkedItemId = req.body.checkbox;

  Item.findByIdAndRemove(checkedItemId, function(err){
    if (err) {
      console.log(err);
    } else {
      console.log("Succesfully deleted.");
      res.redirect("/");
    }
  });
});



app.get("/about", function (req, res) {
  res.render("about");
});

app.listen(3000, function () {
  console.log("Server started on port 3000");
});
