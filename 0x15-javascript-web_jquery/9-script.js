#!/usr/node/bin/node
// 9-script.js
// fetches and prints the San Francisco wind speed by using this URL: https://www.fourtonfish.com/hellosalut/?lang=fr

$.get('https://www.fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
}
);