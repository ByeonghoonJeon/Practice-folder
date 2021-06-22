var numberOfDrumButtons = document.querySelectorAll(".drum").length;


for (var i = 0; i < numberOfDrumButtons; i++) {
  document.querySelectorAll(".drum")[i].addEventListener("click", function () {
    var buttonInnerHTML = this.innerHTML;

    switch (buttonInnerHTML) {
      case "w":
        let crashAudio= new Audio("sounds/crash.mp3");
        crashAudio.play();
        break;
        

      case "a":
        let kickBassAudio = new Audio("sounds/kick-bass.mp3");
        kickBassAudio.play();
        break;

      case "s":
          let snareAudio = new Audio("sounds/snare.mp3");
          snareAudio.play();
          break;
    
      case "d":
          let tom1Audio = new Audio("sounds/tom-1.mp3");
          tom1Audio.play();
          break;
        
      case "j":
          let tom2Audio = new Audio("sounds/tom-2.mp3");
          tom2Audio.play();
          break;
        
      case "k":
          let tom3Audio = new Audio ("sounds/tom-3.mp3");
          tom3Audio.play();
          break;

      case "l":
          let tom4Audio = new Audio ("sounds/tom-4.mp3");
          tom4Audio.play();
          break;
        
      default:
        break;
    }

    if (this.style.color === "white"){
        this.style.color="#DA0463"}else{
            this.style.color="white"
        }
  });
}

document.addEventListener("keydown", function(event){
    switch (event.key) {
        case "w":
          let crashAudio= new Audio("sounds/crash.mp3");
          crashAudio.play();
          document.querySelector(".w",".drum").style.color="white";
          break;
          
  
        case "a":
          let kickBassAudio = new Audio("sounds/kick-bass.mp3");
          kickBassAudio.play();
          document.querySelector(".a", ".drum").style.color="white";
          break;
  
        case "s":
            let snareAudio = new Audio("sounds/snare.mp3");
            snareAudio.play();
            document.querySelector(".s", ".drum").style.color="white";
            break;
      
        case "d":
            let tom1Audio = new Audio("sounds/tom-1.mp3");
            tom1Audio.play();
            document.querySelector(".d", ".drum").style.color="white";
            break;
          
        case "j":
            let tom2Audio = new Audio("sounds/tom-2.mp3");
            tom2Audio.play();
            document.querySelector(".j", ".drum").style.color="white";
            break;
          
        case "k":
            let tom3Audio = new Audio ("sounds/tom-3.mp3");
            tom3Audio.play();
            document.querySelector(".k", ".drum").style.color="white";
            break;
  
        case "l":
            let tom4Audio = new Audio ("sounds/tom-4.mp3");
            tom4Audio.play();
            document.querySelector(".l", ".drum").style.color="white";
            break;
          
        default:
          break;
      }
      
      
});



function workerDatabase(name, gender, age, department){
    this.name = name;
    this.gender = gender;
    this.age = age;
    this.department = department;
    this.clean = function (){
        alert ("Cleaning");
    }
}

let worker1 = new workerDatabase("Nathan", "M", 20, "DD");
