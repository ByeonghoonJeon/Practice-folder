for (var n = 0; n<7; n++){
document.querySelectorAll("button")[n].addEventListener("click",audio);}

var audio = new Audio("sounds/tom-1.mp3");


function audio(){audio.play()}


