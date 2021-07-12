//jshint esversion:6

// calling mongoose.
const { ObjectID } = require('mongodb');
const mongoose = require('mongoose');
const ObjectId = require('mongodb').ObjectID;

// connecting mongoose.
mongoose.connect('mongodb://localhost:27017/fruitsDB', {useNewUrlParser: true, useUnifiedTopology: true});


//mongoose needs schema which is a blue print of data structure.
// const fruitSchema = new mongoose.Schema ({
//     _id: String,
//     name: String,
//     score: Number,
//     review: String
// });


//collection creation, insert with singular form and it will be converted to plural form.
const Fruit = mongoose.model('Fruit', {
    _id: String,
    name: String,
    score: Number,
    review: String
});

//Creating a document from the model.
const fruit = new Fruit(
    {
    _id: ObjectID(), 
    name:"Peach",
    score: 10,
    review: "It's a perfect fruits!"
    },
    {
    _id: ObjectID(), 
    name: 'Banana',
    score: 8,
    review: "Awesome fruit!"
    },
    {   
    _id: ObjectID(), 
    name: 'Apple',
    score: 4,
    review: "Not really.."
    }
);
fruit.save();

// const personSchema = new mongoose.Schema({
//     name: String,
//     age: Number
// });

// const Person = mongoose.model("Person", personSchema);
// const person = new Person({
//     name: "Nathan",
//     age: 19
// });
// person.save();
console.log("Working!")