const $addItem = $('DIV#add_item');

$addItem.on('click', function () {
  let newItem = $('<li>Item</li>');

  $('.my_list').append(newItem);
});
