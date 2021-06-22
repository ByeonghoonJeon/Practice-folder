var numberOfDrumButtons = document.querySelectorAll(".drum").length;

for (var i = 0; i < numberOfDrumButtons; i++) {
  document.querySelectorAll(".drum")[i].addEventListener("click", function () {
    var buttonInnerHTML = this.innerHTML;

    switch (buttonInnerHTML) {
      case "w":
        let crashAudio = new Audio("sounds/crash.mp3");
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
        let tom3Audio = new Audio("sounds/tom-3.mp3");
        tom3Audio.play();
        break;

      case "l":
        let tom4Audio = new Audio("sounds/tom-4.mp3");
        tom4Audio.play();
        break;

      default:
        break;
    }
    function buttonAnimation(){
        let clickedButton = document.querySelector(`.${buttonInnerHTML}`);
        clickedButton.style.color="white";
        clickedButton.classList.add("pressed");
        setTimeout(function(){
            clickedButton.style.color = "#DA0463"
        }, 100);
        setTimeout(function(){
            clickedButton.classList.remove("pressed")
        }, 50);
    }
    buttonAnimation();
  });
}

document.addEventListener("keydown", function (event) {
  switch (event.key) {
    case "w":
      let crashAudio = new Audio("sounds/crash.mp3");
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
      let tom3Audio = new Audio("sounds/tom-3.mp3");
      tom3Audio.play();
      break;

    case "l":
      let tom4Audio = new Audio("sounds/tom-4.mp3");
      tom4Audio.play();
      break;

    default:
      break;
  }

  function buttonAnimation(){
    let clickedButton = document.querySelector(`.${event.key}`);
    clickedButton.style.color="white";
    clickedButton.classList.add("pressed");
    setTimeout(function(){
        clickedButton.style.color = "#DA0463"
    }, 50);
    setTimeout(function(){
        clickedButton.classList.remove("pressed")
    }, 50);
}
buttonAnimation();
});

function workerDatabase(name, gender, age, department) {
  this.name = name;
  this.gender = gender;
  this.age = age;
  this.department = department;
  this.clean = function () {
    alert("Cleaning");
  };
}

let worker1 = new workerDatabase("Nathan", "M", 20, "DD");
