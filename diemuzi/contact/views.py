from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from contact import forms
from contact import models
from form.mixin import SearchMixin
from login.mixin import GaclMixin


class Delete(GaclMixin, generic.DeleteView):
    permission_required = (
        'contact.view_contact',
        'contact.delete_contact'
    )

    model = models.Contact

    success_url = reverse_lazy('contact:search')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Message has been removed.'))

        return super(self.__class__, self).delete(request, *args, **kwargs)


class Index(SuccessMessageMixin, generic.CreateView):
    form_class = forms.FormContact

    template_name = 'contact/index.html'

    success_url = reverse_lazy('contact:index')

    success_message = _('Thank you for contacting us!')


class Read(GaclMixin, generic.DetailView):
    permission_required = (
        'contact.view_contact'
    )

    model = models.Contact

    template_name = 'contact/read.html'


class Search(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'contact.view_contact'
    )

    form_class = forms.FormSearch

    template_name = 'contact/search.html'

    ordering = '-date_from'

    paginate_by = 10

    def get_queryset(self):
        return models.Contact.search(**self.kwargs)
