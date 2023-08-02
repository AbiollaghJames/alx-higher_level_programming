const $h = $('header');
const $divRHeader = $('div#red_header');

$divRHeader.on('click', function () {
  $h.css('color', '#FF0000');
});
