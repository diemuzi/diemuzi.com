from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
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

        default_permissions = ()
