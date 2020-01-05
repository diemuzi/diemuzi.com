from django import forms

from cook import models


class FormAdd(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.fields['category'].choices = models.Category.choices()

    class Meta:
        model = models.Cook

        fields = [
            'account',
            'category',
            'description',
            'directions',
            'image',
            'ingredients',
            'is_featured',
            'keyword',
            'name',
            'serve',
            'time_cook',
            'time_prep'
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
        model = models.Cook

        fields = [
            'category',
            'description',
            'directions',
            'image',
            'ingredients',
            'is_featured',
            'keyword',
            'name',
            'serve',
            'time_cook',
            'time_prep'
        ]

        widgets = {'keyword': forms.TextInput}


class FormSearch(forms.ModelForm):
    class Meta:
        model = models.Cook

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
        model = models.Cook

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
