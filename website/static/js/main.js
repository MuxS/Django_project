var sw = -1;
$(document).ready(function () {

    var size = $('#wrap').innerWidth();
    var getSize = size / 3;

    $('img').ready(function () {
       $('img').css('width', getSize);
    });

    $('#hide').click(function () {
            $('img').fadeToggle(700);
            if (sw == -1) {
                setTimeout(function () {
                    $('#hide').animate({top: '13%'}, 1000);
                    setTimeout(function () {
                        $('#hide').css('background-color', '#FFFFFF');
                    }, 1000);
                    sw *= -1;
                }, 700);
            } else {
                setTimeout(function () {
                    $('#hide').css('background-color', '#858281');
                    $('#hide').animate({top: '30%'}, 1000);
                    sw *= -1;
                }, 10);
            }
    });

    $('img').click(function() {

    })
});