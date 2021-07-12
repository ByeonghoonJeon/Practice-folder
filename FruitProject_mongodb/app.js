//jshint esversion:6

const MongoClient = require("mongodb").MongoClient;
const assert = require("assert");

// Connection URL
const url = "mongodb://localhost:27017";

// Use connect method to connect to the Server
MongoClient.connect(url, { useUnifiedTopology: true }, async function (err, client) {
  assert.equal(null, err);
  const db = client.db("fruits");

  await db.collection("fruits")
    .insertMany([
    {
        name: "Apple",
        score: 8,
        revies: "Great fruit"
    },
    {
        name: "Orange",
        score: 6,
        review: "Kinda sour"
    },
    {
        name: "Banana",
        score: 9,
        review: "Great stuff!"

    }

    ])

  console.log("Working");
  client.close();
});
