from django import forms
from django.utils.translation import gettext as _


class FormComment(forms.Form):
    comment_new = forms.CharField(
        label=_('New Comment'),
        required=True,
        widget=forms.Textarea()
    )
