async function formOnSubmit(event) {
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

  document.querySelector(".date").textContent = getDate();
  document.querySelector("#queryDate").setAttribute("value", fullDate);



  // const queryCity = cityName;
  // const queryDate = document.querySelector("#queryDate");
  // console.log(queryDate);

  // const apiKey = "zo8PEy0GntMaMlKdsCm8yXkWsw47axquHRdVAaLr0b8t3KI8j6IEUeQpAyHmtAHbaT8%2FsuZ5Yo%2FNKycge5d5LQ%3D%3D";
  // const units = "metric";
  // const url =
  //   "https://api.odcloud.kr/api/15077756/v1/vaccine-stat" +
  //   "?serviceKey=" +
  //   apiKey;

  // const infoRequest = await axios.get(url);





}

// apiKey1 zo8PEy0GntMaMlKdsCm8yXkWsw47axquHRdVAaLr0b8t3KI8j6IEUeQpAyHmtAHbaT8%2FsuZ5Yo%2FNKycge5d5LQ%3D%3D
// apiKey2 zo8PEy0GntMaMlKdsCm8yXkWsw47axquHRdVAaLr0b8t3KI8j6IEUeQpAyHmtAHbaT8/suZ5Yo/NKycge5d5LQ==