function add(num1, num2) {return num1+num2;}
function multiply(num1, num2) {return num1*num2;}
function division(num1, num2) {return num1/num2;}
function minus(num1, num2) {return num1-num2;}
function calculator (num1, num2, operator) {return operator (num1, num2);}
var result = operator (num1, num2);
function add(num3) {return result+num3;}
function multiply(num3) {return result*num3;}
function division(num3) {return result/num3;}
function minus(num3) {return result-num3;}
function calculator (num3, operator) {return operator (result, num3);}
result = operator (result, num3);
