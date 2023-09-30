function initMap() {

    map = new google.maps.Map(document.getElementById("map"), {
    center: { latitude, longitude },
    zoom: 10
    });
    getResults(location);
}
  
function getResults(location) {
    let userLocation = new google.maps.LatLng(location.lat, location.long)
    let request = {
        location: userLocation,
        radius: '10000',
        type: ['park'],
        keyword: 'dog'
    }
    service = new google.maps.places.PlacesService(map)
    service.nearbySearch(request, callback)
}


