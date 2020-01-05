from django.http import JsonResponse
from django.shortcuts import resolve_url


def json_redirect(url, *args, **kwargs):
    """
    Redirects using a JsonResponse

    :param str url: URL / Namespace
    :param args: Arguments
    :param dict kwargs: Keyword Arguments

    :return: JsonResponse
    """

    return JsonResponse(
        {
            'success': True,
            'redirect': resolve_url(url, *args, **kwargs)
        }
    )
