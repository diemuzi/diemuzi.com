from django.http import Http404
from django.shortcuts import _get_queryset


def get_latest_object_or_404(klass, *args):
    queryset = _get_queryset(klass)

    try:
        return queryset.latest(*args)

    except queryset.model.DoesNotExist:
        raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)
