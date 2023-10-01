
const searchForm = document.querySelector('#search-form')
const searchInput = document.querySelector('#search-input')
const submitButton = document.querySelector('#submit-button')
let city = ""

const resultBox = document.querySelector('#res_box')
const boxContainer = document.querySelector('#box-container')

function search(event) {
    event.preventDefault()

    if (searchInput.value === "") {
        console.error('Please enter a city for your search!')
        return;
    }

    city = searchInput.value

    geocode(city)
    
}

submitButton.addEventListener('click', search)