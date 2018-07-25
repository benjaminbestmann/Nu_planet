var map;

function initialize() {
  // Create a map centered in Pyrmont, Sydney (Australia).
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8666, lng: 151.1958},
    zoom: 15
  });

  // Search for Google's office in Australia.
  var request = {
    location: map.getCenter(),
    radius: '500',
    query: 'Google Sydney'
  };

  var service = new google.maps.places.PlacesService(map);
  service.textSearch(request, callback);
}

// Checks that the PlacesServiceStatus is OK, and adds a marker
// using the place ID and location from the PlacesService.
function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    var marker = new google.maps.Marker({
      map: map,
      place: {
        placeId: results[0].place_id,
        location: results[0].geometry.location
      }
    });
  }
}

google.maps.event.addDomListener(window, 'load', initialize);



/*window.onload = function(){
  main();
}

function main(){
let searchButton = document.getElementById("searchButton");
searchButton.addEventListener("click", createUrl);

}
function createUrl(search){
  let user_input = document.getElementById("search");
  document.getElementById("map").src = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAQw6VVsR22oM5DCilaaXDEk5VOQKnLq9w&q=" + user_input.value;
  console.log(document.getElementById("map").src);
  console.log(user_input.value);
}
*/
