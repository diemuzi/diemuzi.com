from django import template

from utils import filters

register = template.Library()


@register.filter(name='template_isdefined')
def isdefined(item):
    """
    Check if string has data

    Will return True if data exists, else False

    :param str|int|float|None item: Item to test with

    :return: bool
    """

    return filters.isdefined(item)
