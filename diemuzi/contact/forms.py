from django import forms

from contact import models


class FormContact(forms.ModelForm):
    class Meta:
        model = models.Contact

        fields = [
            'name',
            'email',
            'message'
        ]
