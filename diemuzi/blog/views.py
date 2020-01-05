from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from blog import forms
from blog import models
from form.mixin import SearchMixin
from login.mixin import GaclMixin


class AdminAdd(GaclMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = (
        'blog.view_blog',
        'blog.add_blog'
    )

    model = models.Blog

    form_class = forms.FormAdd

    template_name = 'blog/admin/add.html'

    success_url = reverse_lazy('blog:admin-search')

    success_message = _('Created blog.')


class AdminAddCategory(GaclMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = (
        'blog.view_category',
        'blog.add_category'
    )

    form_class = forms.FormAddCategory

    template_name = 'blog/admin/add_category.html'

    success_url = reverse_lazy('blog:admin-search-category')

    success_message = _('Created category.')


class AdminDelete(GaclMixin, generic.DeleteView):
    permission_required = (
        'blog.view_blog',
        'blog.delete_blog'
    )

    model = models.Blog

    success_url = reverse_lazy('blog:admin-search')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Blog has been removed.'))

        return super(self.__class__, self).delete(request, *args, **kwargs)


class AdminDeleteCategory(GaclMixin, generic.DeleteView):
    permission_required = (
        'blog.view_category',
        'blog.delete_category'
    )

    model = models.Category

    success_url = reverse_lazy('blog:admin-search-category')

    def delete(self, request, *args, **kwargs):
        if self.get_object().can_delete():
            messages.success(self.request, _('Category has been removed.'))

            return super(self.__class__, self).delete(request, *args, **kwargs)
        else:
            messages.warning(self.request, _('Category is currently in use and cannot be removed.'))

            return redirect(self.success_url)


class AdminProfile(GaclMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = (
        'blog.view_blog',
        'blog.change_blog'
    )

    model = models.Blog

    form_class = forms.FormProfile

    template_name = 'blog/admin/profile.html'

    success_url = reverse_lazy('blog:admin-search')

    success_message = _('Updated blog.')


class AdminSearch(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'blog.view_blog'
    )

    form_class = forms.FormSearch

    template_name = 'blog/admin/search.html'

    ordering = '-name'

    paginate_by = 10

    def get_queryset(self):
        return models.Blog.search(**self.kwargs)


class AdminSearchCategory(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'blog.view_category'
    )

    form_class = forms.FormSearchCategory

    template_name = 'blog/admin/search_category.html'

    ordering = 'name'

    paginate_by = 10

    def get_queryset(self):
        return models.Category.search(**self.kwargs)


class Index(SearchMixin, generic.DetailView):
    template_name = 'blog/read.html'

    form_class = forms.FormSearchGlobal

    def get_object(self, queryset=None):
        return get_object_or_404(models.Blog, is_featured=True)


class Read(SearchMixin, generic.DetailView):
    model = models.Blog

    form_class = forms.FormSearchGlobal

    template_name = 'blog/read.html'


class Search(SearchMixin, generic.ListView):
    form_class = forms.FormSearchGlobal

    template_name = 'blog/search.html'

    ordering = '-date_from'

    paginate_by = 9

    def get_queryset(self):
        return models.Blog.search(**self.kwargs)
