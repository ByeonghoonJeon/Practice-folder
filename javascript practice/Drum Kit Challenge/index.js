var audio = new Audio("sounds/tom-1.mp3");
audio.play();
for (var n = 0; n<7; n++){
document.querySelectorAll("button")[n].addEventListener("click",function(){
var audio = new Audio("sounds/tom-1.mp3");
audio.play();
})}


//querySelector("class>children") is for direct children of class
//uerySelector("class .children") is for all the element decendant of class(including not direct)