from django import forms

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


class FormProfile(forms.ModelForm):
    class Meta:
        model = models.Account

        fields = [
            'first_name',
            'last_name',
            'email',
            'locale',
            'time_zone',
            'time_format',
            'comment_order',
            'help_text',
            'form_display'
        ]
