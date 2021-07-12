//jshint esversion:6

// calling mongoose.
const { ObjectID } = require('mongodb');
const mongoose = require('mongoose');

// connecting mongoose.
mongoose.connect('mongodb://localhost:27017/fruitsDB', {useNewUrlParser: true, useUnifiedTopology: true});


//mongoose needs schema which is a blue print of data structure.
const fruitSchema = new mongoose.Schema ({
    _id: new ObjectID(),
    name: String,
    score: Number,
    review: String
});


//collection creation, insert with singular form and it will be converted to plural form.
const Fruit = mongoose.model('Fruit', fruitSchema);

//Creating a document from the model.
const fruit = new Fruit({ 
    name:"Peach",
    score: 10,
    review: "It's a perfect fruits!"
},
{
    name: 'Banana',
    score: 8,
    review: "Awesome fruit!"
},
{   name: 'Apple',
    score: 4,
    review: "Not really.."
});

fruit.save();