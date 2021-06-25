const express = require("express");
const request = require("request");
const app = express();
const https = require("https");
app.use(express.json());
app.use(express.urlencoded());
app.use(express.static('public'));

app.get("/", function(req,res){
    res.sendFile(__dirname+"/public/signup.html");
});

app.post("/", function(req,res){
    const firstName = req.body.firstName;
    const lastName = req.body.lastName;
    const email = req.body.email;

    const data = {
        members: [
            {
                email_address: email,
                status: "subscribed",
                merge_fields: {
                    FNAME: firstName,
                    LNAME: lastName
                }
            }
        ]
    };

    const jsonData=JSON.stringify(data);
    const url = "https://us6.api.mailchimp.com/3.0/lists/ea756b17bc";
    const options = {
        method: "POST",
        auth: s// "Name:API key
    }
    


    const request = https.request(url, options, function(response){
        response.on("data", function(data){
            console.log(JSON.parse(data));
        })
    })
    request.write(jsonData);
    request.end();
    
    
    res.write(firstName);
    res.write(lastName);
    res.write(email);
    res.send();
});


app.listen(3000, function(){
    console.log("Server is running.");
});

//ea756b17bc


