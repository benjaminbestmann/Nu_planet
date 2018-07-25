window.onload = function(){
  main();
}

main = function(){
  let sign_out = document.getElementById("signout");
  sign_out.onclick = signOut;
  var emailInput = document.getElementById('emailInput');
  console.log(emailInput);
  emailInput.value = localStorage["user_email"];
};


function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  var userdata = {
            "id": profile.getId(),
            "fullname": profile.getName(),
            "givenname": profile.getGivenName(),
            "imageurl": profile.getImageUrl(),
            "email": profile.getEmail(),
  };
  console.log("ID: " + profile.getId());
  console.log('Full Name: ' + profile.getName());
  console.log('Given Name: ' + profile.getGivenName());
  console.log("Image URL: " + profile.getImageUrl());
  console.log("Email: " + profile.getEmail());
  var id_token = googleUser.getAuthResponse().id_token;
  console.log("ID Token: " + id_token);
  // document.getElementById('user').innerText = "Welcome to NuPlanet " + profile.getGivenName();
  sendData(userdata);
  localStorage["user_email"] = profile.getEmail();
  window.location.href = "/user";
}
function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    console.log('User signed out.');
    window.location.href = "/";
  });
}

function sendData(data){
  var xhr = new XMLHttpRequest();
  xhr.open("POST", '/data', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  var actualObject = {'data': data}
  xhr.send(JSON.stringify(actualObject));
}
