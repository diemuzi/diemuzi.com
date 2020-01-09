from django import forms

from photo import models


class FormAdd(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.fields['album'].choices = models.Album.choices()

    class Meta:
        model = models.Photo

        fields = [
            'account',
            'album',
            'description',
            'image',
            'is_featured',
            'name'
        ]

        widgets = {'keyword': forms.TextInput}


class FormAddAlbum(forms.ModelForm):
    class Meta:
        model = models.Album

        fields = [
            'name'
        ]


class FormProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.fields['album'].choices = models.Album.choices()

    class Meta:
        model = models.Photo

        fields = [
            'album',
            'description',
            'image',
            'is_featured',
            'name'
        ]

        widgets = {'keyword': forms.TextInput}


class FormSearch(forms.ModelForm):
    class Meta:
        model = models.Photo

        fields = [
            'name',
            'album'
        ]


class FormSearchAlbum(forms.ModelForm):
    class Meta:
        model = models.Album

        fields = [
            'name'
        ]


class FormSearchGlobal(forms.ModelForm):
    class Meta:
        model = models.Photo

        fields = [
            'name',
            'album'
        ]

        widgets = {'keyword': forms.TextInput}

        help_texts = {
            'name': '',
            'album': ''
        }
