function fetchTranslation(languageCode) {
  $.ajax({
    url: "https://www.fourtonfish.com/hellosalut/hello/", 
    type: "GET",
    data: {lang: languageCode},
    dataType: "json",
    success: function (data) {
      $("#hello").text(data.hello);
    },
  });
}
//on click
$(document).ready(function () {
  $("#btn_translate").on('click', function () {
    let languageCode = $("#language_code").val();
    fetchTranslation(languageCode);
  });
//on key press
$("language_code").on('keypress', function(event) {
  if (event.which === 13) {
    let languageCode = $("language_code").val();
    fetchTranslation(languageCode)
  }
  });
});
