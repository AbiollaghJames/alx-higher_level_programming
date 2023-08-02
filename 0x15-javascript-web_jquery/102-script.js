$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    let lang_code = $('INPUT#language_code').val();
    $.ajax({
      url: "https://www.fourtonfish.com/hellosalut/hello/",
      type: "GET",
      dataType: "json",
      success: function(data) {
        $("#hello").text(data.hello);
      }
    });
  });
});
