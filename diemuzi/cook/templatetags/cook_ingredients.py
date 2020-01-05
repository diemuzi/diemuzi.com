from django import template

from cook import models

register = template.Library()


@register.simple_tag(name='cook_ingredients')
def ingredients(obj):
    """
    Ingredients

    :param models.Cook obj: Cook Object

    :return: str
    """

    return obj.ingredients.split('--')
