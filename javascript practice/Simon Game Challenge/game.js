
const gamePattern = [];
const buttonColours = ["red", "blue", "green", "yellow"];

function nextSequence(){
    const randomisation = Math.random()*4;
    const randomNumber = Math.floor(randomisation);
    return randomNumber;
}

const randomChosenColour = buttonColours[nextSequence()];
gamePattern.push(randomChosenColour);

$(`#${randomChosenColour}`).fadeOut(100).fadeIn(100);

switch (randomChosenColour) {
    case "yellow":
        let yellowSound = new Audio("sounds/yellow.mp3");
        yellowSound.play();
        break;
    
    case "red":
        let redSound = new Audio("sounds/red.mp3");
        redSound.play();
        break;
    
    case "blue":
        let blueSound = new Audio ("sounds/blue.mp3");
        blueSound.play();
        break

    case "green":
        let greenSound = new Audio ("sounds/blue.mp3");
        greenSound.play();
        break


    default:
        let randomSound = new Audio("sounds/yellow.mp3");
        randomSound.play();
        break;
}

