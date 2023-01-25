#!/usr/bin/node
// change the text color of the HTML tag HEADER to red (#FF0000) using jquery api

$('DIV#red_header').click(function () {
    $('HEADER').css('color', '#FF0000')
})
