const ranFloat1 = Math.random()*6;
const randomNumber1 = Math.floor(ranFloat1)+1;
let imgSource1 = "";

const ranFloat2 = Math.random()*6;
const randomNumber2 = Math.floor(ranFloat2)+1;
let imgSource2 = "";

switch (randomNumber1) {
    case 1:
        imgSource1 = "images/dice1.png";
        
        break;

    case 2:
        imgSource1 = "images/dice2.png";
        
        break;

    case 3:
        imgSource1 = "images/dice3.png";
        
        break;
    
    case 4:
        imgSource1 = "images/dice4.png";
        
        break;

    case 5:
        imgSource1 = "images/dice5.png";
        
        break;

    case 6:
        imgSource1 = "images/dice6.png";
        
        break;  
    
    default:
        console.log("The number is not 1");
        break;
};


switch (randomNumber2) {
    case 1:
        imgSource2 = "images/dice1.png";
        
        break;

    case 2:
        imgSource2 = "images/dice2.png";
        
        break;

    case 3:
        imgSource2 = "images/dice3.png";
        
        break;
    
    case 4:
        imgSource2 = "images/dice4.png";
        
        break;

    case 5:
        imgSource2 = "images/dice5.png";
        
        break;

    case 6:
        imgSource2 = "images/dice6.png";
        
        break;  
    
    default:
        console.log("The number is not 1");
        break;
};
document.body.querySelector(".img1").setAttribute("src", imgSource1);
document.body.querySelector(".img2").setAttribute("src", imgSource2);

if (randomNumber1>randomNumber2){
    document.body.querySelector("h1").innerHTML="Player 1 Win!"
} else if (randomNumber1<randomNumber2){
    document.body.querySelector("h1").innerHTML="Player 2 Win!"
} else {
    document.body.querySelector("h1").innerHTML="Draw!"
};
