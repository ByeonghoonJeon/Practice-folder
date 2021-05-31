const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");
const https = require("https");


const app = express();


app.use(bodyParser.urlencoded({extended: true}));


app.get("/", function (req,res){
    res.sendFile(__dirname + "/signup.html");
    
});

app.use(express.static(__dirname));

app.post("/",function(req,res){
    const firstName = req.body.fName;
    const lastName = req.body.lName;
    const email = req.body.eMail;

    const data = {
        members: [
            {
                email_address:email,
                status: "subscribed",
                merge_field: {
                     FNAME: firstName,
                     LNAME: lastName
                }
            }
        ]
    };

    const jsonData = JSON.stringify(data);
    const url = "https://us6.api.mailchimp.com/3.0/lists/ea756b17bc";
    const options = {
        method:"POST",
        auth: "byeonghoon1:b27f02810ee29a6ac7d2d03ec32076c5-us6"
    }
   
    const request = https.request(url, options, function(response){
        if (response.statusCode === 200){
            res.send("Successfully subscribed!");
        }
        else {
            res.send("There was an error with signing up. Please try again.")
        }
        response.on("data", function(data){
        console.log(JSON.parse(data));
    })
    })
    request.write(jsonData);
    console.log(firstName,lastName,email)
    request.end();
});
   
app.listen(3000,function(){
    console.log("Server is running on port 3000");
})


// API Key
// b27f02810ee29a6ac7d2d03ec32076c5-us6
// audience ID
// ea756b17bc