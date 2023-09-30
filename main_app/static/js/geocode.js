let latitude;
let longitude;

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
      console.log('Latitude:', latitude);
      console.log('Longitude:', longitude);

      response.innerText = JSON.stringify(result, null, 2);
      return results;
    })
    .catch((e) => {
      alert("Geocode was not successful for the following reason: " + e);
    });
}

function clear() {
  marker.setMap(null);
  responseDiv.style.display = "none";
}

