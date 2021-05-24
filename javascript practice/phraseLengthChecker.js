var writingLimit = 140;
var opinion = prompt("Write your opinion.");
var currentLength = opinion.length;
var availableLength = writingLimit - currentLength;
alert ("You have written "+currentLength+" letters and you have "+availableLength+" letters more.");
var under140 = opinion.slice(0,140);
if (currentLength>=140){alert ("Your opinion exceeds 140 letters. It will be shown as following: "+under140)};