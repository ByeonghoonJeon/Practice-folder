async function formOnSubmit(event) {
  
  // get city name from form input value
  console.log(event);
  // get form data
  const formData = new FormData(event.target);
  console.log(formData);
  // convert to object
  const formProps = Object.fromEntries(formData);
  console.log(formProps);

  // access cityName from object
  // const queryDate = formProps.queryDate;
  // console.log(queryDate);

  const queryDate = document.querySelector("#queryDate").value;
  console.log(queryDate);
  const apiKey = "zo8PEy0GntMaMlKdsCm8yXkWsw47axquHRdVAaLr0b8t3KI8j6IEUeQpAyHmtAHbaT8%2FsuZ5Yo%2FNKycge5d5LQ%3D%3D";
  const url =
    "https://api.odcloud.kr/api/15077756/v1/vaccine-stat" + "?cond%5BbaseDate%3A%3AGT%5D=" + queryDate + "&serviceKey=" + apiKey;

  const infoRequest = await axios.get(url);
  
  const vaccinationInfo = infoRequest.data;
  console.log(vaccinationInfo);
  // const fullTemp = weatherData.main.temp;
  // const temp = fullTemp.toFixed(1);
  // const weatherDescription = weatherData.weather[0].description;
  // console.log(weatherDescription);




}
function getDate() {
  const today = new Date();
  const options = { weekday: "long", day: "numeric", month: "long" };
  return today.toLocaleDateString("en-US", options);
}

let date = new Date();
let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();

if (day < 10) {
  day = "0" + day;
}

if (month < 10) {
  month = "0" + month;
}

let fullDate = `${year}-${month}-${day}`;

console.log(fullDate);

document.querySelector(".headerDate").textContent = getDate();
document.querySelector("#queryDate").setAttribute("value", fullDate);
// apiKey1 zo8PEy0GntMaMlKdsCm8yXkWsw47axquHRdVAaLr0b8t3KI8j6IEUeQpAyHmtAHbaT8%2FsuZ5Yo%2FNKycge5d5LQ%3D%3D
// apiKey2 zo8PEy0GntMaMlKdsCm8yXkWsw47axquHRdVAaLr0b8t3KI8j6IEUeQpAyHmtAHbaT8/suZ5Yo/NKycge5d5LQ==