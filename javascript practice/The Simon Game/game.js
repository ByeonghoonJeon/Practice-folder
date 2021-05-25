var buttonColours = ["red", "blue", "green", "yellow"];
var gamePattern = [];
function nextSequence(){
    var ranNumber = Math.floor(Math.random()*4);
    var randomChosenColour = buttonColours[ranNumber];
    gamePattern.push(randomChosenColour);

}
$("#"+randomChosenColour).addEventListener("click",function(){
    alert("Got clicked");})