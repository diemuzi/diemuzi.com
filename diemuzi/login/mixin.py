from django.conf import settings
from django.contrib import messages
from django.contrib.auth import mixins
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


class GaclMixin(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin):
    """
    Override LoginRequiredMixin & PermissionRequiredMixin

    Sets a message, redirect, and removes the ?next= URL
    """

    def __init__(self, **kwargs):
        self.request = kwargs.pop('request', None)

        super(__class__, self).__init__()

        self.kwargs = kwargs

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.add_message(self.request, messages.ERROR, _('GACL: You must be logged in.'))
        else:
            messages.add_message(self.request, messages.ERROR, _('GACL: You do not have the proper permissions.'))

        try:
            return super(GaclMixin, self).handle_no_permission()
        except PermissionDenied:
            return HttpResponseRedirect(settings.LOGIN_URL)
