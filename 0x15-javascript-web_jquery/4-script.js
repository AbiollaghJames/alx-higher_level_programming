const $h = $('header');
const $toggleHeader = $('DIV#toggle_header');

$toggleHeader.on('click', function () {
  let headerElem = $('header');
  if (headerElem.hasClass('red')) {
    headerElem.removeClass('red').addClass('green');
  }
  else {
    headerElem.removeClass('green').addClass('red');
  }
});
