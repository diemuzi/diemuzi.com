from django.db import transaction
from django.http import JsonResponse
from django.views import generic

from form.redirects import json_redirect


class AjaxResponseMixin(generic.FormView):
    """
    Mixin to add AJAX support to a form.

    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)

        if self.request.is_ajax():
            return JsonResponse(form.errors)
        else:
            return response

    @transaction.atomic()
    def form_valid(self, form):
        # Inject Request Object
        form.request = self.request

        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)

        if self.request.is_ajax():
            return json_redirect(self.get_success_url())
        else:
            return response


class SearchMixin(generic.FormView):
    def get_initial(self):
        initial = super(SearchMixin, self).get_initial()

        for key, value in self.kwargs.copy().items():
            initial[key] = value

        return initial
