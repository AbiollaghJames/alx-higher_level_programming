const $toClick = $('DIV#update_header');
const $h = $('header');

$toClick.on('click', function () {
  $h.text('New Header!!!');
});
