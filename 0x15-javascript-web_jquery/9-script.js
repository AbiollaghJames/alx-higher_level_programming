const apiUrl = "https://fourtonfish.com/hellosalut/?lang=fr";

$.ajax ({
  url: apiUrl,
  type: "GET",
  dataType: "json",
  success: function(data){
    $("DIV#hello").text(data.hello);
  }
});
