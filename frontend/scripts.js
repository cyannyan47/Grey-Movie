// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/test', true)

request.onload = function () {
  // Begin accessing JSON data here
}

// Send request
request.send()

// Begin accessing JSON data here
var data = JSON.parse(this.response)

data.forEach((movie) => {
  // Log each movie's title
  console.log(movie.title)
})