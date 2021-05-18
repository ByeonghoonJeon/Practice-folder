// Set a function.
function fibonacciCode(finalNumber){
// Set initial Fibonacci order.
var fibonacci = [0, 1]
// Initial "n" is zero, final n is finalNumber-2, and add 1 for every loop. And add to the array.
for (var n=0; n<finalNumber-2; n++){
    fibonacci.push(fibonacci[n]+fibonacci[n+1])}
    return (fibonacci)
}
fibonacciCode()


