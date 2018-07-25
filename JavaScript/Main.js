ß

window.onload = function(){
  main();
}

function main(){
let searchButton = document.getElementById("searchButton");
searchButton.addEventListener("click", grabUserInput);

}
function grabUserInput(){
  let user_input = document.getElementById("search");
  document.getElementById("map").src = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAQw6VVsR22oM5DCilaaXDEk5VOQKnLq9w&q=" + user_input.value;
  console.log(document.getElementById("map").src);
  console.log(user_input.value);
}
