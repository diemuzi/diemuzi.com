from django.http import HttpResponseNotFound


def handle_400(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def handle_403(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def handle_404(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def handle_500(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')
