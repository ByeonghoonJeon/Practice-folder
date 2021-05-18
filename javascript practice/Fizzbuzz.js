
var userNumber = [];
var countNumber = 1;
function fizzbuzz(){

if (countNumber%3===0 && countNumber%5===0){userNumber.push("FizzBuzz")};
if (countNumber%3 === 0) {userNumber.push("Fizz")};
if (countNumber%5 === 0) {userNumber.push("Buzz")};
if (countNumber%3 !== 0 && countNumber%5 !==0){userNumber.push(countNumber)};
countNumber++;
alert(userNumber);
}
