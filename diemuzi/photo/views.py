from django.views import generic


class Index(generic.TemplateView):
    template_name = 'photo/coming_soon.html'
