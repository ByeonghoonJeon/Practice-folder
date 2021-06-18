const ranFloat = Math.random()*6;
const randomNumber1 = Math.floor(ranFloat)+1;
let imgSource = document.querySelector(".img1").src;

switch (randomNumber1) {
    case 1:
        imgSource = "images/dice1.png";
        
        break;

    case 2:
        imgSource = "images/dice2.png";
        
        break;

    case 3:
        imgSource = "images/dice3.png";
        
        break;
    
    case 4:
        imgSource = "images/dice4.png";
        
        break;

    case 5:
        imgSource = "images/dice5.png";
        
        break;

    case 6:
        imgSource = "images/dice6.png";
        
        break;  
    
    default:
        console.log("The number is not 1");
        break;
};
document.body.querySelector(".img1").setAttribute("src", imgSource)
console.log(imgSource);