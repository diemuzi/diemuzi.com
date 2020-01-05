from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from cook import forms
from cook import models
from form.mixin import SearchMixin
from login.mixin import GaclMixin


class AdminAdd(GaclMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = (
        'cook.view_cook',
        'cook.add_cook'
    )

    model = models.Cook

    form_class = forms.FormAdd

    template_name = 'cook/admin/add.html'

    success_url = reverse_lazy('cook:admin-search')

    success_message = _('Created recipe.')


class AdminAddCategory(GaclMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = (
        'cook.view_category',
        'cook.add_category'
    )

    form_class = forms.FormAddCategory

    template_name = 'cook/admin/add_category.html'

    success_url = reverse_lazy('cook:admin-search-category')

    success_message = _('Created category.')


class AdminDelete(GaclMixin, generic.DeleteView):
    permission_required = (
        'cook.view_cook',
        'cook.delete_cook'
    )

    model = models.Cook

    success_url = reverse_lazy('cook:admin-search')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Recipe has been removed.'))

        return super(self.__class__, self).delete(request, *args, **kwargs)


class AdminDeleteCategory(GaclMixin, generic.DeleteView):
    permission_required = (
        'cook.view_category',
        'cook.delete_category'
    )

    model = models.Category

    success_url = reverse_lazy('cook:admin-search-category')

    def delete(self, request, *args, **kwargs):
        if self.get_object().can_delete():
            messages.success(self.request, _('Category has been removed.'))

            return super(self.__class__, self).delete(request, *args, **kwargs)
        else:
            messages.warning(self.request, _('Category is currently in use and cannot be removed.'))

            return redirect(self.success_url)


class AdminProfile(GaclMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = (
        'cook.view_cook',
        'cook.change_cook'
    )

    model = models.Cook

    form_class = forms.FormProfile

    template_name = 'cook/admin/profile.html'

    success_url = reverse_lazy('cook:admin-search')

    success_message = _('Updated recipe.')


class AdminSearch(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'cook.view_category'
    )

    form_class = forms.FormSearch

    template_name = 'cook/admin/search.html'

    ordering = '-name'

    paginate_by = 10

    def get_queryset(self):
        return models.Cook.search(**self.kwargs)


class AdminSearchCategory(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'cook.view_category'
    )

    form_class = forms.FormSearchCategory

    template_name = 'cook/admin/search_category.html'

    ordering = 'name'

    paginate_by = 10

    def get_queryset(self):
        return models.Category.search(**self.kwargs)


class Index(SearchMixin, generic.DetailView):
    template_name = 'cook/read.html'

    form_class = forms.FormSearchGlobal

    def get_object(self, queryset=None):
        return get_object_or_404(models.Cook, is_featured=True)


class Read(SearchMixin, generic.DetailView):
    model = models.Cook

    form_class = forms.FormSearchGlobal

    template_name = 'cook/read.html'


class Search(SearchMixin, generic.ListView):
    template_name = 'cook/search.html'

    form_class = forms.FormSearchGlobal

    paginate_by = 9

    def get_queryset(self):
        return models.Cook.search(**self.kwargs)
