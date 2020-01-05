/**
 * Modals
 */
$(function () {
    /**
     * Delete Modal
     */
    $('#search').on('click', '.btn-delete', function () {
        let url = $(this).attr('data-url');

        $('#delete_modal').modal('show');

        $('#modal_url_delete').attr('action', url);
    });

    /**
     * Search Modal
     */
    $('#search_modal :submit').on('click', function (event) {
        event.preventDefault();

        let values = '';

        $.each($('#search_modal :input').serializeArray(), function (i, field) {
            if (field.name !== 'csrfmiddlewaretoken' && field.value !== '') {
                values += '/' + field.name + '/' + field.value;
            }
        });

        window.location = $('#search_modal').attr('action') + values;
    });

    $('#search_modal_clear').on('click', function (event) {
        event.preventDefault();

        window.location = $('#search_modal').attr('action');
    });
});