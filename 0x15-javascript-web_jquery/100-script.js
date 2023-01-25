#!/usr/bin/node
// updates color 
document.addEventListener('DOMContentLoaded', function () {
    $('DIV#update_header').click(function () {
        $('HEADER').text('New Header!!!');
    });
}
);