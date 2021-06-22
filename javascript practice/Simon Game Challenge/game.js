
const gamePattern = [];
const buttonColours = ["red", "blue", "green", "yellow"];

function nextSequence(){
    const randomisation = Math.random()*3;
    const randomNumber = Math.floor(randomisation)+1;
    const randomChosenColour = buttonColours[randomNumber];
    return randomChosenColour;
}
console.log(nextSequence());
gamePattern.push(nextSequence());

console.log(gamePattern);