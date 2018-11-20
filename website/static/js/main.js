$(document).ready(function () {

    var size = $('#wrap').innerWidth();
    var getSize = size / 3;

    $('img').ready(function () {
       $('img').css('width', getSize);
    });
});