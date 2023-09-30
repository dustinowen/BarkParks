import './geocode.js'

function initMap() {

    map = new google.maps.Map(document.getElementById("map"), {
    center: { latitude, longitude },
    zoom: 10
    });
    getResults(location);
}
  
function getResults(location) {
    let userLocation = new google.maps.LatLng(latitude, longitude)
    let request = {
        location: userLocation,
        radius: '10000',
        type: ['park'],
        keyword: 'dog'
    }
    service = new google.maps.places.PlacesService(map)
    service.nearbySearch(request, callback)
}

function callback(results, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        cardContainer.innHTML = ""
        for (let i = 0; i < results.length; i++) {
            let place = results[i]
            console.log(results)
            let content = '<div> < h5 > ${ place.name }</h5> <p>${place.vicinity}</p></div>'

            //build out display area for results
            const res_box = document.createElement("div")
            const name = document.createElement("h4")
            const address = document.createElement("p")
            
            name.append(place.name)
            address.append(place.vicinity)
            
            //disperse results over created areas
            res_box.setAttribute("class", "card")
            cardContainer.append(res_box)
            res_box.append(name)
            res_box.append(address)

            //created custom marker with dog icon
            let marker = new google.maps.Marker({
                position: place.geometry.location,
                map: map,
                title: place.name,
                label: "🐶",
            })

            let info_box = new google.maps.InfoWindow({ content: content })

            groupInfoWindow(marker, map, info_box, content)
            marker.setMap(map)
        }
    }

    //created event listener for marker clicks to display results information
    function groupInfoWindow(marker, map, info_box, html) {
        marker.addListener('click', function () {
            info_box.setContent(html)
            info_box.open(map, this)
        })
    }

}
