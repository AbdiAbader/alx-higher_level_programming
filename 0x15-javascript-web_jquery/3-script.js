#!/usr/bin/node
// 3-script.js
// change the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header
$('DIV#red_header').click(function () {
    $('HEADER').addClass('red')
});