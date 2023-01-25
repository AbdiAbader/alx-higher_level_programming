#!/usr/bin/node
//  jQuery API #5 - Add, Remove, and Toggle HTML Classes

$('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
});