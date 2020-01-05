from django import template

from cook import models

register = template.Library()


@register.simple_tag(name='cook_category')
def categories():
    """
    Returns a list of cooking recipie categories.

    :return: obj
    """

    return models.Category.categories()
