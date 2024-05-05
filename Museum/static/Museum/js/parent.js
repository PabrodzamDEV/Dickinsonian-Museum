$(window).scroll(function() {
    if ($(window).scrollTop() > 80) {
        $('.navbar').addClass('fixed-top');
    } else {
        $('.navbar').removeClass('fixed-top');
    }
});