#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $('DIV#character').text(data.name);
});