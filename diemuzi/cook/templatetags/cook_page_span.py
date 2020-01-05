from django import template

from cook import models

register = template.Library()


@register.simple_tag(name='cook_next')
def cook_next(cook_object):
    """
    Displays a "Next" page

    :param models.Cook cook_object: Cook Object

    :return: str
    """

    if isinstance(cook_object, models.Cook):
        cook = models.Cook.objects.filter(date_from__gte=cook_object.date_from) \
            .exclude(pk=cook_object.pk).order_by('date_from').first()

        if isinstance(cook, models.Cook):
            return cook


@register.simple_tag(name='cook_previous')
def cook_previous(cook_object):
    """
    Displays a "Previous" page

    :param models.Cook cook_object: Cook Object

    :return: str
    """

    if isinstance(cook_object, models.Cook):
        cook = models.Cook.objects.filter(date_from__lte=cook_object.date_from) \
            .exclude(pk=cook_object.pk).order_by('-date_from').first()

        if isinstance(cook, models.Cook):
            return cook
