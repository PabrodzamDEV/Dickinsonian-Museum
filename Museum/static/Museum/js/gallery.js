$(document).ready(function () {
    $('#galleryModal').on('show.bs.modal', function (event) {
        // Button that triggered the modal
        var button = $(event.relatedTarget);

        // Extract info from data-* attributes
        var pieceUrl = button.data('piece-url');
        var pieceTitle = button.data('piece-title');
        var pieceAuthor = button.data('piece-author');
        var pieceFileType = button.data('piece-filetype');
        var pieceDetailUrl = button.data('piece-detailurl')

        // Update the modal's content
        updateModalContent(pieceUrl, pieceTitle, pieceFileType);

        // Update the modal's title
        var modalTitle = $(this).find('.modal-title');
        modalTitle.html("<b>" + pieceAuthor + "</b>" + "<br>" + "<i>" + pieceTitle + "</i>");

        // Add click event handler for the detail button that takes the user to the detail view
        var butonDetail = $(this).find('.btn-detail');
        butonDetail.click(function(){
            window.location.href = pieceDetailUrl
        });
    });
});

function updateModalContent(pieceUrl, pieceTitle, pieceFileType) {
    var modalBody = $('#galleryModal').find('.modal-body');

    if (pieceFileType === 'image') {
        modalBody.html('<img src="' + pieceUrl + '" alt="' + pieceTitle + '" class="img-fluid">');
    } else if (pieceFileType === 'video') {
        modalBody.html('<video width="100%" height="auto" src="' + pieceUrl + '" type="video/webm" controls autoplay muted>Your browser does not support the video tag.</video>');
    }
}
