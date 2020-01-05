from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )

    comment = models.TextField(
        verbose_name=_('Current Comments'),
        blank=True,
        null=True
    )

    date_from = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On')
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Status')
    )

    class Meta:
        abstract = True
