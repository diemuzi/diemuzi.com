from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from form.mixin import SearchMixin
from login.mixin import GaclMixin
from photo import forms
from photo import models


class AdminAdd(GaclMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = (
        'photo.view_photo',
        'photo.add_photo'
    )

    model = models.Photo

    form_class = forms.FormAdd

    template_name = 'photo/admin/add.html'

    success_url = reverse_lazy('photo:admin-search')

    success_message = _('Created Photo.')


class AdminAddAlbum(GaclMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = (
        'photo.view_album',
        'photo.add_album'
    )

    form_class = forms.FormAddAlbum

    template_name = 'photo/admin/add_album.html'

    success_url = reverse_lazy('photo:admin-search-album')

    success_message = _('Created album.')


class AdminDelete(GaclMixin, generic.DeleteView):
    permission_required = (
        'photo.view_photo',
        'photo.delete_photo'
    )

    model = models.Photo

    success_url = reverse_lazy('photo:admin-search')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Photo has been removed.'))

        return super(self.__class__, self).delete(request, *args, **kwargs)


class AdminDeleteAlbum(GaclMixin, generic.DeleteView):
    permission_required = (
        'photo.view_album',
        'photo.delete_album'
    )

    model = models.Album

    success_url = reverse_lazy('photo:admin-search-album')

    def delete(self, request, *args, **kwargs):
        if self.get_object().can_delete():
            messages.success(self.request, _('Album has been removed.'))

            return super(self.__class__, self).delete(request, *args, **kwargs)
        else:
            messages.warning(self.request, _('Album is currently in use and cannot be removed.'))

            return redirect(self.success_url)


class AdminProfile(GaclMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = (
        'photo.view_photo',
        'photo.change_photo'
    )

    model = models.Photo

    form_class = forms.FormProfile

    template_name = 'photo/admin/profile.html'

    success_url = reverse_lazy('photo:admin-search')

    success_message = _('Updated photo.')


class AdminSearch(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'photo.view_album'
    )

    form_class = forms.FormSearch

    template_name = 'photo/admin/search.html'

    ordering = '-name'

    paginate_by = 10

    def get_queryset(self):
        return models.Photo.search(**self.kwargs)


class AdminSearchAlbum(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'photo.view_album'
    )

    form_class = forms.FormSearchAlbum

    template_name = 'photo/admin/search_album.html'

    ordering = 'name'

    paginate_by = 10

    def get_queryset(self):
        return models.Album.search(**self.kwargs)


class Index(SearchMixin, generic.ListView):
    model = models.Album

    template_name = 'photo/index.html'

    form_class = forms.FormSearchGlobal

    paginate_by = 9


class Search(SearchMixin, generic.ListView):
    template_name = 'photo/search.html'

    form_class = forms.FormSearchGlobal

    paginate_by = 9

    def get_queryset(self):
        return models.Photo.search(**self.kwargs)
