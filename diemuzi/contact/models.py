from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    date_from = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On')
    )

    email = models.EmailField(
        validators=[
            validators.MinLengthValidator(5),
            validators.EmailValidator
        ],
        verbose_name=_('Email Address'),
        blank=False,
        null=False
    )

    message = models.TextField(
        blank=False,
        null=False
    )

    name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ],
        verbose_name=_('Name'),
        blank=False,
        null=False
    )

    class Meta:
        db_table = 'contact'

        default_permissions = ('view', 'delete')

    def __str__(self):
        return self.name

    @staticmethod
    def search(**kwargs):
        search_params = {
            'name': 'icontains',
            'email': 'icontains'
        }

        query = {}

        for key, value in kwargs.items():
            if value is None:
                del kwargs[key]

            if key in search_params:
                query[key + '__' + search_params[key]] = kwargs[key]

        return Contact.objects.filter(**query)
