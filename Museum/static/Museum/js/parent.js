window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.querySelector('.navbar').classList.add('fixed-top');
    } else {
        document.querySelector('.navbar').classList.remove('fixed-top');
    }
}