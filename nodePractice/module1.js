function myFunction(){
    console.log("Function is called");
    }

var myString = "String!";
module.exports.myFunction = myFunction; //When function itself is not required to be executed, paranthesis is not included.
module.exports.myString = myString;
