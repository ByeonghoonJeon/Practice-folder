
const gamePattern = [];
const buttonColours = ["red", "blue", "green", "yellow"];

function nextSequence(){
    const randomisation = Math.random()*3;
    const randomNumber = Math.floor(randomisation)+1;
    return randomNumber;
}

const randomChosenColour = buttonColours[nextSequence()];
console.log(randomChosenColour);
gamePattern.push(randomChosenColour);
console.log(gamePattern);

$(`#${randomChosenColour}`).fadeOut(100).fadeIn(100);
$(`#${randomChosenColour}`).