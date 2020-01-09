from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from comment import models as comment_models


class Album(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z0-9 -]+$')
        ],
        verbose_name=_('Name'),
        blank=False,
        null=False,
        help_text=_('Name of album.')
    )

    slug = models.SlugField(
        max_length=255,
        verbose_name=_('Slug Name'),
        blank=False,
        null=False
    )

    class Meta:
        db_table = 'photo_album'

        models.Index(
            fields=['slug']
        )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)

        super(self.__class__, self).save()

    def can_delete(self):
        related = Photo.objects.filter(album=self)

        if related.exists():
            return False

        return True

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        if 'name' not in exclude and self.name and self.validate_name():
            raise ValidationError({'name': _('Name already exists.')})

    def validate_name(self):
        return Album.objects.filter(Q(name__iexact=self.name) | Q(slug__iexact=slugify(self.name))).exists()

    @staticmethod
    def albums():
        """
        Get a list of albums and how many photos there are

        :return: list
        """

        return Photo.objects.values('album__name', 'album__slug').annotate(count=models.Count('pk'))

    @staticmethod
    def choices():
        """
        Photo Album Choices

        :return: list
        """

        empty = [
            (None, '---------')
        ]

        result = empty + [
            (item.pk, item.name) for item in Album.objects.all()
        ]

        if len(result) == 0:
            return empty

        return result

    def featured(self):
        return Photo.objects.get(album=self, is_featured=True)

    def photos(self):
        return Photo.objects.filter(album=self)

    @staticmethod
    def search(**kwargs):
        search_params = {
            'name': 'icontains'
        }

        query = {}

        for key, value in kwargs.items():
            if value is None:
                del kwargs[key]

            if key in search_params:
                query[key + '__' + search_params[key]] = kwargs[key]

        return Album.objects.filter(**query)


def photo_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/photo/<album>/<filename>
    return 'photo/{0}/{1}'.format(instance.album, filename)


class Photo(models.Model):
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text=_('Select an album to associate this photo to.')
    )

    date_from = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On')
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name=_('Featured'),
        help_text=_('Choose if this should be featured.')
    )

    name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ],
        verbose_name=_('Name'),
        blank=False,
        null=False,
        help_text=_('Name of the photo.')
    )

    slug = models.SlugField(
        max_length=255,
        verbose_name=_('Slug Name'),
        blank=False,
        null=False
    )

    description = models.TextField(
        verbose_name=_('Description'),
        blank=False,
        null=False,
        help_text=_('Write something fancy.')
    )

    image = models.ImageField(
        verbose_name=_('Photo Image'),
        blank=False,
        null=False,
        upload_to=photo_directory_path,
        help_text=_('The image to display.')
    )

    class Meta:
        db_table = 'photo'

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        if 'name' not in exclude and self.name and self.validate_name():
            raise ValidationError({'name': _('Name already exists.')})

    def validate_name(self):
        return Photo.objects.filter(Q(name__iexact=self.name) | Q(slug__iexact=slugify(self.name))).exclude(
            pk=self.pk).exists()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)

        super(self.__class__, self).save()

    @staticmethod
    def comments():
        return Comment.objects.filter(is_active=True)

    @staticmethod
    def search(**kwargs):
        search_params = {
            'name': 'icontains',
            'album': 'exact|slug'
        }

        query = {}

        for key, value in kwargs.items():
            if value is None:
                del kwargs[key]

            if key in search_params:
                if '|' in search_params[key]:
                    try:
                        if int(kwargs[key]):
                            query[key + '__' + search_params[key].split('|')[0]] = kwargs[key]
                    except ValueError:
                        query[key + '__' + search_params[key].split('|')[1]] = kwargs[key]
                else:
                    query[key + '__' + search_params[key]] = kwargs[key]

        return Photo.objects.filter(**query)


class Comment(comment_models.Comment):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )

    class Meta:
        db_table = 'comment_photo'
