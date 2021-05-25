$("h1").css("color", "red");

$("h1").addClass("center_title");
$("button").html("<em>Click it</em>");

for (var n = 0; n < 5; n++) {
  document.querySelectorAll("button")[n].addEventListener("click", function () {
    document.querySelector("h1").style.color = "blue";
  });
}

for (var i = 0; i < 5; i++) {
  $("button")[i].addEventListener("click", function () {
    $("h1").css("color", "white");
  });
}
