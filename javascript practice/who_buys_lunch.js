// Programm that determins who will pay for the lunch with randomization function.//

nameList = ["Alex", "Nathan", "Sophia", "Sahrah", "Tom", "Edwin", "Thisler"]
var n = Math.random();
lengthNameList = nameList.length;
n = n*(lengthNameList);
floorNumber = Math.floor(n);
alert (nameList[floorNumber]+" will pay for our lunch!");

