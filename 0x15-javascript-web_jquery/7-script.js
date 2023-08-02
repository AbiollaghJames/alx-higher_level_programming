const apiUrl = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
const $display = $('DIV#character');

$.ajax ({
  url: apiUrl,
  type: "GET",
  dataType: "json",
  success: function (data) {
    let charName = data.name;
    $display.text(charName);
  }
});
