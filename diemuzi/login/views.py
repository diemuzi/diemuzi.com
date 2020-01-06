from django.contrib import messages
from django.contrib.admin import forms as admin_forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from form.mixin import SearchMixin
from login import forms
from login import models
from login.mixin import GaclMixin


class Access(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'login.view_accesslog'
    )

    form_class = forms.FormAccess

    template_name = 'login/access.html'

    ordering = '-date_from'

    paginate_by = 10

    def get_queryset(self):
        return models.AccessLog.search(account_id=self.request.user.id, **self.kwargs)


class Create(SuccessMessageMixin, generic.CreateView):
    template_name = 'login/create.html'

    form_class = forms.FormCreate

    success_url = reverse_lazy('login:login')

    success_message = _('Thank you for registering. Check your email for your login information.')


class Delete(GaclMixin, generic.DeleteView):
    permission_required = (
        'login.view_account',
        'login.delete_account'
    )

    model = models.Account

    success_url = reverse_lazy('login:logout')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.is_superuser:
            messages.add_message(request, messages.INFO, _('Administrator account cannot be removed.'))

            return redirect(self.success_url)
        else:
            messages.success(self.request, _('Account has been removed.'))

            return super(Delete, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(models.Account, pk=self.request.user.id)


class Index(SuccessMessageMixin, LoginView):
    template_name = 'login/login.html'

    form_class = admin_forms.AuthenticationForm


class Password(GaclMixin, SuccessMessageMixin, PasswordChangeView):
    permission_required = (
        'login.view_password'
    )

    form_class = PasswordChangeForm

    template_name = 'login/password.html'

    success_url = reverse_lazy('login:password')

    success_message = _('Updated account password.')


class Permission(GaclMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = (
        'login.view_permission',
        'login.change_permission'
    )

    model = models.Account

    form_class = forms.FormPermission

    template_name = 'login/permission.html'

    success_message = _('Updated user permissions.')

    def get_form_kwargs(self):
        kwargs = super(Permission, self).get_form_kwargs()

        kwargs['group_perm'] = self.get_object().get_group_permissions()
        kwargs['user_perm'] = self.get_object().get_user_permissions()

        return kwargs

    def get_success_url(self):
        return reverse_lazy('login:permission', kwargs={'pk': self.kwargs['pk']})


class Profile(GaclMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = (
        'login.view_account'
    )

    model = models.Account

    form_class = forms.FormProfile

    template_name = 'login/profile.html'

    success_url = reverse_lazy('login:profile')

    success_message = _('Updated account profile.')

    def get_object(self, queryset=None):
        return get_object_or_404(models.Account, pk=self.request.user.id)


class ProfileManage(GaclMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = (
        'login.view_manage'
    )

    form_class = forms.FormProfileManage

    template_name = 'login/profile_manage.html'

    success_message = _('Updated user profile.')

    def get_object(self, queryset=None):
        return models.Account.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('login:profile-manage', kwargs={'pk': self.kwargs['pk']})


class Search(GaclMixin, SearchMixin, generic.ListView):
    permission_required = (
        'login.view_manage'
    )

    form_class = forms.FormSearch

    template_name = 'login/search.html'

    ordering = ('last_name', 'first_name')

    paginate_by = 10

    def get_queryset(self):
        return models.Account.search(**self.kwargs)
