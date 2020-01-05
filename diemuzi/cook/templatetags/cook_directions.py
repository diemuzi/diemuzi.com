from django import template

from cook import models

register = template.Library()


@register.simple_tag(name='cook_directions')
def directions(obj):
    """
    Directions

    :param models.Cook obj: Cook Object

    :return: str
    """

    return obj.directions.split('--')
