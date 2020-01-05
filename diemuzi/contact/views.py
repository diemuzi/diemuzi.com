from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from contact import forms


class Index(SuccessMessageMixin, generic.CreateView):
    form_class = forms.FormContact

    template_name = 'contact/index.html'

    success_url = reverse_lazy('contact:index')

    success_message = _('Thank you for contacting us!')
