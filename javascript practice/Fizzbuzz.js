var userNumber = [];
var countNumber = 1;
function fizzbuzz(){

if (countNumber%3===0 && countNumber%5===0){userNumber.push("FizzBuzz")};
if (countNumber%3 === 0 && countNumber%5 !== 0) {userNumber.push("Fizz")};
if (countNumber%5 === 0 && countNumber%3 !==0) {userNumber.push("Buzz")};
if (countNumber%3 !== 0 && countNumber%5 !==0){userNumber.push(countNumber)};
countNumber++;
alert(userNumber);
}

while (countNumber <= 100){fizzbuzz()}

/* for loop example.
for (start-point; end-point; changes;) */
for (var i = 1; i<2; i++){console.log(i);}