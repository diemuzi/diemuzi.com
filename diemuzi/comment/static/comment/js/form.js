/**
 * Modal Comments
 */
$(function () {
    $('#commentOpen').on('click', function () {
        let popup = $('#commentModal');

        let popup_url = $('#form_comment').attr('action');

        let popup_body = $('.modal-body');

        popup_body.load(popup_url);

        popup.modal('show');
    });
});

/**
 * Ajax Form Validation Handler
 * Only used for Modal Comments
 */
$(function () {
    /**
     * Form ID
     */
    let form = $('#form_comment');

    /**
     * Add Class
     */
    form.find('textarea').addClass('form-control');

    /**
     * Remove Class
     */
    //form.find('input[type="submit"]').removeClass('form-control');

    let submit = $('#submit_comment');

    /**
     * Submit Form
     */
    submit.on('click',
        function () {
            /**
             * Show Spinner on Submit Button
             */
            submit
                .after('<i class="fas fa-spinner fa-pulse fa-lg" id="busy_comment"></i>')
                .hide();

            /**
             * Get all form fields
             * @type {FormData}
             */
            let form_data = new FormData(form[0]);

            /**
             * Configure
             * @type {*|*|*|*}
             */
            let process = $.ajax(
                {
                    type: 'POST',
                    url: form.attr('action'),
                    dataType: 'json',
                    data: form_data,
                    processData: false,
                    contentType: false,
                    cache: false
                }
            );

            /**
             * Process Form
             */
            process.done(
                function (response) {
                    /**
                     * Form looks good, process and redirect
                     */
                    if (response.success) {
                        window.location = response.redirect;
                    }

                    /**
                     * Create an array of Form Fields
                     */
                    let array = {};

                    for (let key of form_data.keys()) {
                        array[key] = '';
                    }

                    /**
                     * Invalid Fields
                     * Reverse the order so we get the first error
                     */
                    $.each(
                        response, function (key, value) {
                            $.each(
                                value.reverse(), function (message_key, message_value) {
                                    array[key] = message_value;
                                }
                            );
                        }
                    );

                    /**
                     * Remove Icons
                     */
                    $('.form-control-feedback').remove();

                    /**
                     * Filter the array
                     */
                    $.each(
                        array, function (key, value) {
                            let nameKey = $('#id_' + key);

                            let inputKey = $('#input-' + key);

                            if ($('#id_' + key + '-status').is(':visible')) {
                                $('span[id^="id_' + key + '-status"]').remove();
                            }

                            $('label').addClass('form-control-label');

                            /**
                             * Invalid Fields
                             */
                            if (value !== '') {
                                /**
                                 * All Visable Elements Except CSRF
                                 */
                                if (key !== 'csrfmiddlewaretoken' && nameKey.is(':visible')) {
                                    inputKey.find('textarea')
                                        .removeClass('is-valid')
                                        .addClass('is-invalid');

                                    nameKey.after('<span id="id_' + key + '-status" class="form-text text-danger">' + value + '</span>');
                                }
                            }

                            /**
                             * Valid Fields
                             */
                            if (value === '') {
                                /**
                                 * All Element Except CSRF
                                 */
                                if (key !== 'csrfmiddlewaretoken' && nameKey.is(':visible')) {
                                    inputKey.find('textarea')
                                        .removeClass('is-invalid')
                                        .addClass('is-valid');
                                }
                            }
                        }
                    );
                }
            );

            /**
             * Cleanup once form submission has completed
             */
            process.always(
                function () {
                    /**
                     * Show Submit Button
                     */
                    submit.show();

                    /**
                     * Remove Spinner on Submit Button
                     */
                    $('#busy_comment').hide();
                }
            );

            return false;
        }
    );
});