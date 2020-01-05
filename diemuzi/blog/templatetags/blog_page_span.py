from django import template

from blog import models

register = template.Library()


@register.simple_tag(name='blog_next')
def blog_next(blog_object):
    """
    Displays a "Next" page

    :param models.Blog blog_object: Blog Object

    :return: str
    """

    if isinstance(blog_object, models.Blog):
        blog = models.Blog.objects.filter(date_from__gte=blog_object.date_from) \
            .exclude(pk=blog_object.pk).order_by('date_from').first()

        if isinstance(blog, models.Blog):
            return blog


@register.simple_tag(name='blog_previous')
def blog_previous(blog_object):
    """
    Displays a "Previous" page

    :param models.Blog blog_object: Blog Object

    :return: str
    """

    if isinstance(blog_object, models.Blog):
        blog = models.Blog.objects.filter(date_from__lte=blog_object.date_from) \
            .exclude(pk=blog_object.pk).order_by('-date_from').first()

        if isinstance(blog, models.Blog):
            return blog
