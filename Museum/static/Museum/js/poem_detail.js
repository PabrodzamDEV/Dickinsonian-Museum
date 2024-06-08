$(document).ready(function() {
    $('.more-poems').hover(
        function() {
            $('.poem-list').css('display', 'inline-block');
            $('#envelope').attr('src', '/static/Museum/images/envelope-open.svg');
        },
        function() {
            $('.poem-list').css('display', 'none');
            $('#envelope').attr('src', '/static/Museum/images/envelope-closed.svg');
        }
    );
});
