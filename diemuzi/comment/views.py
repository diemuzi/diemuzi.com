from pydoc import locate

from django.apps import apps
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import mixins
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.views import generic

from comment import forms
from form.mixin import AjaxResponseMixin
from form.redirects import json_redirect


class Add(mixins.LoginRequiredMixin, AjaxResponseMixin, generic.FormView):
    form_class = forms.FormComment

    template_name = 'comment/comment.html'

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = models.Comment.objects.filter(**{
            self.kwargs['object_name']: self.kwargs['object_id']
        }).order_by('-date_from')

        return context"""

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            model = next((m for m in apps.get_models() if m._meta.db_table == self.kwargs.get('object_name')), None)

            account = (get_object_or_404(get_user_model(), pk=request.user.id) if request.user else None)

            this_class = locate("%s.models.Comment" % model._meta.db_table)

            # models.Comment.objects.create(
            #    made_by=made_by,
            #    comment=form.cleaned_data['comment_new'],
            # )

            this_class.objects.create(
                account=account,
                comment=form.cleaned_data['comment_new'],
                **{
                    str(model._meta.db_table) + '_id': self.kwargs['object_id']
                }
            )

            messages.add_message(request, messages.SUCCESS, _('Comment was added'))

            return json_redirect(self.get_success_url())

        return JsonResponse(form.errors)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
