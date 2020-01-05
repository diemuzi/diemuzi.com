from django.views import generic


class Faq(generic.TemplateView):
    template_name = 'home/faq.html'


class Index(generic.TemplateView):
    template_name = 'home/index.html'


class Privacy(generic.TemplateView):
    template_name = 'home/privacy.html'
