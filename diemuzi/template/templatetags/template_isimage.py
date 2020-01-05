from django import template

from utils import filters

register = template.Library()


@register.filter(name='template_isimage')
def image(item):
    """
    Check if image exists

    :param object item: Item to test with

    :return: bool
    """

    return filters.isimage(item)
