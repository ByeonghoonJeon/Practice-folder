


var audio = new Audio("sounds/tom-1.mp3");
audio.play();
for (var n = 0; n<7; n++){
document.querySelectorAll("button")[n].addEventListener("click",function(){
var audio = new Audio("sounds/tom-1.mp3");
audio.play();
})}
document.querySelector("button").addEventListener("click", handleClick);
function handleClick(){alert ("I got clicked!");}

