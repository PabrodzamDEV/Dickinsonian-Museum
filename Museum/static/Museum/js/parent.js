$(window).scroll(function() {
    if ($(window).scrollTop() > 1) {
        $('.navbar').addClass('fixed-top');
    } else {
        $('.navbar').removeClass('fixed-top');
    }
});