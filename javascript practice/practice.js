//Java script study note.

alert("Hello");
alert("World");
alert(2+3);

typeof("STR S$5")
/* When a programmer makes a variable*/
var myname = "Nathan";
/* When a programmer overwrites excisting variable*/
myname = "Jeon";

var greeting = "Hello";
var myName = "Nathan";

alert(greeting + myName)

lenthMessage = promt ("Compose your message");

var message = prompt("Please write your message")
var countLetter = message.length
alert ("You have written "+countLetter+" characters and you have "+(140-countLetter)+" letters more.")

// Slice practice
var message = prompt ("Please type your message");
var countMessage = message.length;
alert ("You have written "+countMessage+" letters and "+(200-countMessage)+" letter(s) are available.")
alert (message.slice(0,10));

// Practice: Whatever user inputs his name, make the first letter upper case and lower cases for else.

var userName = prompt("Please input your name");
var firstLetter = userName.slice(0,1);
var firstUpperLetter=firstLetter.toUpperCase();
var elseLetters = userName.slice(1,userName.length);
var elseLowerLetters = elseLetters.toLowerCase();
alert ("Hello, "+firstUpperLetter+elseLowerLetters);


// Dog age calculator
var dogYear = prompt("Please input your dot's age");
var dogAgeConvert = (dogYear-2)*4+21;
alert ("Your dog's age is "+dogAgeConvert + " in human age.");

// Increment and Decrement
var x = 5;
x = x +1;
x ++;
x+=3 // x = x+3

var y = 5;
y = y-1
y --;


// Creation of Function.

function messageCounting(){
userName = prompt("Please input your name");
userMessage = prompt("Please type your message");
MessageCount = userMessage.length
alert("Your message is "+MessageCount+" letters.");}

messageCounting()

//Randomisation

var n = Math.random();
n = n*6;
n=Math.floor(n)+1;
console.log(n);

// Is equal to
a === b
// Is not equal to
a !== b
// Is greater than
a > b
// Is lesser than
a < b
// Is greater or equal than
a >= b
// Is lesser or equal than
a <= b
