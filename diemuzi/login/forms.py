from django import forms
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db.models import Q

from login import models


class FormAccess(forms.ModelForm):
    class Meta:
        model = models.AccessLog

        fields = [
            'ipaddress',
            'reverse_ipaddress'
        ]

        widgets = {
            'reverse_ipaddress': forms.TextInput
        }


class FormCreate(forms.ModelForm):
    class Meta:
        model = models.Account

        fields = [
            'email',
            'first_name',
            'last_name'
        ]

    def save(self, commit=True):
        instance = super(FormCreate, self).save(commit=False)

        instance.create_account()

        return instance


class FormPermission(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        group_perm = kwargs.pop('group_perm')
        user_perm = kwargs.pop('user_perm')

        super(FormPermission, self).__init__(*args, **kwargs)

        def related(initial):
            perms = []

            for item in initial:
                perm = item.split('.')

                permission = auth_models.Permission.objects.get(content_type__app_label=perm[0], codename=perm[1])

                perms.append(permission.pk)

            return perms

        related_group = related(group_perm)
        related = related(user_perm)

        self.fields['default'].queryset = auth_models.Permission.objects.filter(pk__in=related_group).exclude(
            content_type__app_label__in=settings.EXCLUDE_GROUP_APPS)

        self.fields['permission'].queryset = auth_models.Permission.objects.all().exclude(
            Q(content_type__app_label__in=settings.EXCLUDE_GROUP_APPS) | Q(pk__in=related_group))

        self.fields['permission'].initial = related

    default = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'readonly': True}),
        queryset=None,
        required=False
    )

    permission = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple,
        required=False,
        queryset=None
    )

    class Meta:
        model = auth_models.Permission

        fields = [
            'default',
            'permission'
        ]

    def save(self, commit=True):
        instance = super(FormPermission, self).save(commit=False)

        instance.user_permissions.clear()

        for item in self.cleaned_data['permission']:
            try:
                gacl = auth_models.Permission.objects.get(pk=item.pk)

                instance.user_permissions.add(gacl)
            except auth_models.Permission.DoesNotExist:
                pass

        return instance


class FormProfile(forms.ModelForm):
    class Meta:
        model = models.Account

        fields = [
            'comment_order',
            'email',
            'first_name',
            'form_display',
            'help_text',
            'last_name',
            'locale',
            'time_format',
            'time_zone'
        ]


class FormProfileManage(forms.ModelForm):
    class Meta:
        model = models.Account

        fields = [
            'comment_order',
            'email',
            'first_name',
            'form_display',
            'help_text',
            'is_active',
            'last_name',
            'locale',
            'time_format',
            'time_zone'
        ]


class FormSearch(forms.ModelForm):
    class Meta:
        model = models.Account

        fields = [
            'first_name',
            'last_name',
            'email'
        ]
