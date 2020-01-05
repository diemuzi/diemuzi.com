from django import forms

from blog import models


class FormAdd(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.fields['category'].choices = models.Category.choices()

    class Meta:
        model = models.Blog

        fields = [
            'account',
            'category',
            'entry',
            'is_featured',
            'keyword',
            'name',
            'video_url'
        ]

        widgets = {'keyword': forms.TextInput}


class FormAddCategory(forms.ModelForm):
    class Meta:
        model = models.Category

        fields = [
            'name'
        ]


class FormProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.fields['category'].choices = models.Category.choices()

    class Meta:
        model = models.Blog

        fields = [
            'category',
            'entry',
            'is_featured',
            'keyword',
            'name',
            'video_url'
        ]

        widgets = {'keyword': forms.TextInput}


class FormSearch(forms.ModelForm):
    class Meta:
        model = models.Blog

        fields = [
            'name',
            'category'
        ]


class FormSearchCategory(forms.ModelForm):
    class Meta:
        model = models.Category

        fields = [
            'name'
        ]


class FormSearchGlobal(forms.ModelForm):
    class Meta:
        model = models.Blog

        fields = [
            'name',
            'category',
            'keyword'
        ]

        widgets = {'keyword': forms.TextInput}

        help_texts = {
            'name': '',
            'category': '',
            'keyword': ''
        }
