from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from comment import models as comment_models


class Blog(models.Model):
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text=_('Select a category to associate this blog to.')
    )

    date_from = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On')
    )

    entry = models.TextField(
        verbose_name=_('Entry'),
        blank=False,
        null=False,
        help_text=_('Write something fancy.')
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name=_('Featured'),
        help_text=_('Choose if this should be featured.')
    )

    keyword = models.TextField(
        verbose_name=_('Keywords'),
        blank=False,
        null=False,
        help_text=_('Each keyword is an individual token separated by commas.')
    )

    name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ],
        verbose_name=_('Name'),
        blank=False,
        null=False,
        help_text=_('Name of the blog.')
    )

    slug = models.SlugField(
        max_length=255,
        verbose_name=_('Slug Name'),
        blank=False,
        null=False
    )

    video_url = models.URLField(
        verbose_name=_('Video URL'),
        blank=True,
        null=True,
        help_text=_('Link to an embeddable video.')
    )

    class Meta:
        db_table = 'blog'

        models.Index(
            fields=['slug']
        )

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        if 'name' not in exclude and self.name and self.validate_name():
            raise ValidationError({'name': _('Name already exists.')})

    def validate_name(self):
        return Blog.objects.filter(Q(name__iexact=self.name) | Q(slug__iexact=slugify(self.name))).exclude(
            pk=self.pk).exists()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)

        if self.is_featured:
            Blog.objects.all().update(is_featured=False)

        super(self.__class__, self).save()

    @staticmethod
    def comments():
        return Comment.objects.filter(is_active=True)

    def keywords(self):
        return self.keyword.split(',')

    @staticmethod
    def search(**kwargs):
        search_params = {
            'name': 'icontains',
            'category': 'exact|slug',
            'keyword': 'icontains'
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

        return Blog.objects.filter(**query)


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z0-9 ]+$')
        ],
        verbose_name=_('Name'),
        blank=False,
        null=False,
        help_text=_('Name of category.')
    )

    slug = models.SlugField(
        max_length=255,
        verbose_name=_('Slug Name'),
        blank=False,
        null=False
    )

    class Meta:
        db_table = 'blog_category'

        models.Index(
            fields=['slug']
        )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)

        super(self.__class__, self).save()

    def can_delete(self):
        related = Blog.objects.filter(category=self)

        if related.exists():
            return False

        return True

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        if 'name' not in exclude and self.name and self.validate_name():
            raise ValidationError({'name': _('Name already exists.')})

    def validate_name(self):
        return Category.objects.filter(Q(name__iexact=self.name) | Q(slug__iexact=slugify(self.name))).exists()

    @staticmethod
    def categories():
        """
        Get a list of categories and how many artciles there are

        :return: list
        """

        return Category.objects.values('name', 'slug').annotate(count=models.Count('pk'))

    @staticmethod
    def choices():
        """
        Blog Category Choices

        :return: list
        """

        empty = [
            (None, '---------')
        ]

        result = empty + [
            (item.pk, item.name) for item in Category.objects.all()
        ]

        if len(result) == 0:
            return empty

        return result

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

        return Category.objects.filter(**query)


class Comment(comment_models.Comment):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )

    class Meta:
        db_table = 'comment_blog'
