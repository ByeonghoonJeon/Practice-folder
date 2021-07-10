//jshint esversion:6

const MongoClient = require("mongodb").MongoClient;
const assert = require("assert");

// Connection URL
const url = "mongodb://localhost:27017";

// Use connect method to connect to the Server
MongoClient.connect(url, { useUnifiedTopology: true }, async function (err, client) {
  assert.equal(null, err);
  const db = client.db("test");

  await db.collection("inventory")
    .insertOne({
      item: "canvas",
      qty: 100,
      tags: ["cotton"],
      size: { h: 28, w: 35.5, uom: "cm" },
    })

  console.log("Working");
  client.close();
});
