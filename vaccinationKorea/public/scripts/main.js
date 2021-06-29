function getDate () {
    const today = new Date();
    const options = { weekday: "long", day: "numeric", month: "long" };
    return today.toLocaleDateString("en-US", options);
  };

let date = new Date();
let day = date.getDate();
let month = date.getMonth()+1;
let year = date.getFullYear();

if (day < 10){
  day = "0"+day;
}

if (month <10){
  month = "0"+month;
}

let fullDate = `${year}-${month}-${day}`;

console.log(fullDate);

document.querySelector(".date").textContent = getDate();
document.querySelector("#queryDate").setAttribute("value",fullDate);
