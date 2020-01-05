from django.contrib.auth import mixins
from django.views import generic


class Index(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'member/index.html'
