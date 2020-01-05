from django import template

from blog import models

register = template.Library()


@register.simple_tag(name='blog_category')
def categories():
    """
    Returns a list of blog categories.

    :return: obj
    """

    return models.Category.categories()
