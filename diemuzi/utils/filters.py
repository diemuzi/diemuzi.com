from html.parser import HTMLParser

from django.db.models.fields.files import ImageFieldFile


def isdefined(string):
    """
    Check if value has data

    Will return True if data exists, else False

    :param dict|list|str|int|float|None string: Data to test with

    :return: bool
    """

    if string is None:
        return False
    elif type(string) is str and not string.strip():
        return False
    elif type(string) is str and string == '':
        return False
    elif type(string) is int and not string:
        return False
    elif type(string) is float and not string:
        return False
    elif type(string) is list and len(string) == 0:
        return False
    elif type(string) is dict and len(string) == 0:
        return False
    elif type(string) is bool:
        return True
    elif type(string) is ImageFieldFile and isinstance(string, ValueError):
        return False
    else:
        return True


def isimage(string):
    """
    Check if image exists

    :param object string: Data to test with

    :return: bool|object
    """

    if type(string) is ImageFieldFile:
        try:
            return string
        except ValueError:
            return False

    return string


def strip_html(html):
    """
    Strips HTML from string

    :param str html: HTML string to be removed

    :return: str
    """

    s = MLStripper()
    s.feed(html)

    return s.get_data()


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()

        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)
