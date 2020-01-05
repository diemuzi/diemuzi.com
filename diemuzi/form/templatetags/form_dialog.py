from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

register = template.Library()


@register.simple_tag(name='form_dialog')
def dialog(body, status):
    """
    Modal

    :param str body: Text for modal
    :param str status: Status delete / install / queue

    :return: str
    """

    button_cancel = ''

    button_confirm = ''

    if status == 'delete':
        button_cancel = """
        <button type="button" class="btn btn-default" data-dismiss="modal">
            <i class="fas fa-times" aria-hidden="true"></i> {dialog_cancel}
        </button>
        """.format(dialog_cancel=_('Cancel'))

        button_confirm = """
            <button type="submit" class="btn btn-danger">
                <i class="fas fa-trash-alt fa-1x"></i> {dialog_confirm}
            </button>
        """.format(dialog_confirm=_('Confirm'))

    modal = """
    <!-- Start {status} Modal -->
    <div class="modal fade" id="{status}_modal" tabindex="-1" role="dialog"
         aria-labelledby="{status}_modal_label" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="{status}_modal_label">
                        <i class="fas fa-exclamation-triangle fa-1x text-danger"></i> {dialog_title}
                    </h5>
                    
                    <button type="button" class="close" data-dismiss="modal" aria-label="{dialog_close}">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                
                <div class="modal-body">
                    {dialog_body}
                </div>
                
                <div class="modal-footer">
                    {dialog_cancel}
                    
                    {dialog_confirm}
                </div>
            </div>
        </div>
    </div>
    <!-- End {status} Modal -->
    """.format(
        dialog_title=_('Warning'),
        dialog_body=body,
        dialog_close=_('Close'),
        dialog_cancel=button_cancel,
        dialog_confirm=button_confirm,
        status=status
    )

    return mark_safe(modal)
