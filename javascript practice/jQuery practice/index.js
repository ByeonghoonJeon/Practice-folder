$(".textBox").keydown(function(event){
  let typedText = event.key;
   $("h1").text(typedText);
  console.log(typedText)
});