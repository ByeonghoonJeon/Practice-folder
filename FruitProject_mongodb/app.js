//jshint esversion:6

// calling mongoose.
const { ObjectID } = require('mongodb');
const mongoose = require('mongoose');
const ObjectId = require('mongodb').ObjectID;

// connecting mongoose.
mongoose.connect('mongodb://localhost:27017/fruitsDB', {useNewUrlParser: true, useUnifiedTopology: true});


//mongoose needs schema which is a blue print of data structure.
const fruitSchema = new mongoose.Schema ({
    name: String,
    score: Number,
    review: String
});


//collection creation, insert with singular form and it will be converted to plural form.
const Fruit = mongoose.model('Fruit', fruitSchema);

//Creating a document from the model.
const fruits = [ // this should be a list of fruits not a fruit object (new Fruit) which is just 1 single fruit
    {
        name:"Peach",
        score: 10,
        review: "It's a perfect fruits!"
    },
    {
        name: 'Banana',
        score: 8,
        review: "Awesome fruit!"
    },
    {   
        name: 'Apple',
        score: 4,
        review: "Not really.."
    }
];

Fruit.insertMany(fruits, function(err){ // fruits here instead of [fruit] because we already have an array with fruits
    if (err) {
        console.log(err);
    } else {
        console.log("Successfully saved all the fruits data.")
    }
});

/////////////////////////////////////////////////////


const personSchema = new mongoose.Schema({
    name: String,
    age: Number
});

const Person = mongoose.model("Person", personSchema);
const person = [// should be called people and be a list (array) of people -- see above ^
    {
        name: "Nathan",
        age: 19
    },
    {
        name: "Edwin",
        age: 18
    }
];

Person.insertMany(person, function(err){ // fruits here instead of [fruit] because we already have an array with fruits
    if (err) {
        console.log(err);
    } else {
        console.log("Successfully saved all the people data.")
    }
});


console.log("Working!")

// NOTES:
// have a look here for reference: https://www.geeksforgeeks.org/mongoose-insertmany-function/
// also here is the mongoose documentation which may assist you: https://mongoosejs.com/docs/documents.html

// Important takeaways:
// _id is an automatically generated field used by the database to assign a unique id to each document
// new Fruit() and new Person() are creating a single document from the {} json object within the parenthesis
// insertMany inserts an array of documents or an array of {} json objects which match the schema for the collection
// .save() saves a modified document to the database
// document = new Person()  json object = {}