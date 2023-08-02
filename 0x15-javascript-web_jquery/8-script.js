const apiUrl = "https://swapi-api.alx-tools.com/api/films/?format=json";
const $display = $('UL#list_movies');

$.ajax({
  url: apiUrl,
  type: "GET",
  dataType: "json"
  success: function(data) {
    data.results.forEach(function (movie) {
      $display.append("<li>" + movie.title +"</li>");
    });
  }
});

