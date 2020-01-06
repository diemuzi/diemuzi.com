from django import forms

from contact import models


class FormContact(forms.ModelForm):
    class Meta:
        model = models.Contact

        fields = [
            'email',
            'message',
            'name'
        ]


class FormSearch(forms.ModelForm):
    class Meta:
        model = models.Contact

        fields = [
            'name',
            'email'
        ]
