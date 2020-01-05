from django.views import generic


class Index(generic.TemplateView):
    template_name = 'about/index.html'
