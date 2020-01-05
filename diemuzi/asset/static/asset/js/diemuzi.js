/**
 * Custom
 */
$(function () {
    /**
     * Prevent link from following its href
     */
    $('a[aria-disabled="true"]').on('click', function (event) {
        event.preventDefault();
    });

    /**
     * Message Timeout
     */
    window.setTimeout(
        function () {
            $('.alert-dismissible')
                .alert('close');
        }, 10000
    );

    /**
     * Toggle Side Bar
     */
    $('#toggle_sidebar').on('click', function (event) {
        event.preventDefault();

        $('#sidebar').toggleClass('d-none d-md-block');
    });

    /**
     * To Top Page
     */
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });

    let back_to_top = $('#back-to-top');

    // scroll body to 0px on click
    back_to_top.click(function () {
        $('#back-to-top').tooltip('hide');

        $('body, html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });

    back_to_top.tooltip('show');
});
