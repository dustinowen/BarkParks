let latitude;
let longitude;

let map;
let marker;
let geocoder;
let responseDiv;
let response;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10,
    center: { latitude, longitude},
    mapTypeControl: false,
  });

  geocoder = new google.maps.Geocoder();

  const inputText = document.getElementById("inputText");

  inputText.type = "text";
  inputText.placeholder = "Enter a location";

  const submitButton = document.getElementById("submitButton");

  submitButton.type = "button";
  submitButton.value = "Geocode";
  submitButton.classList.add("button", "button-primary");

  const clearButton = document.getElementById("clearButton");

  clearButton.type = "button";
  clearButton.value = "Clear";
  clearButton.classList.add("button", "button-secondary");

  response = document.createElement("pre");
  response.id = "response";
  response.innerText = "";
  responseDiv = document.createElement("div");
  responseDiv.id = "response-container";
  responseDiv.appendChild(response);

  const instructionsElement = document.createElement("p");

  instructionsElement.id = "instructions";
  instructionsElement.innerHTML =
    "<strong>Instructions</strong>: Enter an address in the textbox to geocode or click on the map to reverse geocode.";

  marker = new google.maps.Marker({
    map,
  });

  map.addListener("click", (e) => {
    geocode({ location: e.latLng });
  });
  submitButton.addEventListener("click", () =>
    geocode({ address: inputText.value })
  );
  clearButton.addEventListener("click", () => {
    clear();
  });

  clear();
}

function clear() {
  marker.setMap(null);
  responseDiv.style.display = "none";
}

function geocode(request) {
  clear();

  geocoder
    .geocode(request)
    .then((result) => {
      const { results } = result;

      map.setCenter(results[0].geometry.location);
      marker.setPosition(results[0].geometry.location);
      marker.setMap(map);
      responseDiv.style.display = "block";

      //Storing latitude and longitude in global variable
      latitude = results[0].geometry.location.lat();
      longitude = results[0].geometry.location.lng();

      // Testing lat/long response (fingers crossed!)
      console.log("Latitude:", latitude);
      console.log("Longitude:", longitude);

      response.innerText = JSON.stringify(result, null, 2);
      return results;
    })
    .catch((e) => {
      alert("Geocode was not successful for the following reason: " + e);
    });

  initMap(latitude, longitude);
}

// function clear() {
//   marker.setMap(null);
//   responseDiv.style.display = "none";
// }

function initMap(lat, long) {
//   let location = new Object();
//   location.lat = newLat;
//   location.long = newLong;

  map = new google.maps.Map(document.getElementById("map"), {
    center: {
      lat: lat,
      lng: long,
    },
    zoom: 10,
  });
  getResults(location);
}

function getResults(location) {
  let userLocation = new google.maps.LatLng(lat, long);
  let request = {
    location: userLocation,
    radius: "10000",
    type: ["park"],
    keyword: "dog",
  };
  service = new google.maps.places.PlacesService(map);
  service.nearbySearch(request, callback);
}

function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    cardContainer.innHTML = "";
    for (let i = 0; i < results.length; i++) {
      let place = results[i];
      console.log(results);
      let content =
        "<div> < h5 > ${ place.name }</h5> <p>${place.vicinity}</p></div>";

      //build out display area for results
      const res_box = document.createElement("div");
      const name = document.createElement("h4");
      const address = document.createElement("p");

      name.append(place.name);
      address.append(place.vicinity);

      //disperse results over created areas
      res_box.setAttribute("class", "card");
      boxContainer.append(res_box);
      res_box.append(name);
      res_box.append(address);

      //created custom marker with dog icon
      let marker = new google.maps.Marker({
        position: place.geometry.location,
        map: map,
        title: place.name,
        label: "🐶",
      });

      let info_box = new google.maps.InfoWindow({ content: content });

      groupInfoWindow(marker, map, info_box, content);
      marker.setMap(map);
    }
  }

  //created event listener for marker clicks to display results information
  function groupInfoWindow(marker, map, info_box, html) {
    marker.addListener("click", function () {
      info_box.setContent(html);
      info_box.open(map, this);
    });
  }
}
