#!/usr/bin/node
// 103-script.js
// fetches and prints the San Francisco wind speed by using this URL: https://www.fourtonfish.com/hellosalut/?lang=fr

$('document').ready(function () {
    $('INPUT#btn_translate').click(function () {
        $('INPUT#btn_translate').focus(function () {
            $(this).keydown(function (event) {
                if (event.which === 13) {
                    event.preventDefault();
                }
            }
            );
        })
    });
});
