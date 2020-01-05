/**
 * BlockUI
 */
$(function () {
    let submit = $('button[type="submit"]');

    submit.on('click', function () {
        $.blockUI(
            {
                message: '<i class="fas fa-spinner fa-pulse fa-5x"></i>',
                css: {
                    '-webkit-border-radius': '10px',
                    '-moz-border-radius': '10px',
                    backgroundColor: '#000',
                    padding: '15px',
                    border: 'none',
                    opacity: .5,
                    color: '#fff'
                }
            }
        );
    })
});