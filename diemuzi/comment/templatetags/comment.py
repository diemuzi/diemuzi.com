from django import template

register = template.Library()


@register.filter(name='comment_table')
def table_name(obj):
    """
    Comment

    :param obj: Foreign Key Object

    :return: str
    """

    return obj._meta.db_table
