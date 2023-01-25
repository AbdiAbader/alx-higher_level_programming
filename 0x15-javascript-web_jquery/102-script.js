#!/usr/bin/node

$('document').ready(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/'
    $('INPUT#btn_translate').click(function () {

        $.get(url, { lang: $('INPUT#language_code').val() }, function (data) {
            $('DIV#hello').text(data.hello);
        }
        );
    });
});