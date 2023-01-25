#!/usr/bin/node
// 8-script.js
// fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    for (let i = 0; i < data.results.length; i++) {
        $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
    }
}
);