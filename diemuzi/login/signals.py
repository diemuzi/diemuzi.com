import socket

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import models as auth_models
from django.utils.translation import activate
from django.utils.translation import gettext as _
from ipware.ip import get_ip

from login import models


def create_group_permissions(sender, **kwargs):
    group, created = auth_models.Group.objects.get_or_create(name='Client')

    for item in settings.GROUP_PERMISSIONS:
        perm = item.split('.')

        permission = auth_models.Permission.objects.exclude(
            content_type__app_label__in=settings.EXCLUDE_GROUP_APPS).get(content_type__app_label=perm[0],
                                                                         codename=perm[1])

        group.permissions.add(permission.pk)


def handle_login(sender, request, user, **kwargs):
    ip = get_ip(request)

    models.AccessLog.objects.create(
        account=user,
        ipaddress=ip,
        reverse_ipaddress=socket.getfqdn(ip)
    )

    request.session['django_language'] = user.locale
    request.session['django_timezone'] = user.time_zone

    activate(user.locale)

    messages.add_message(request, messages.INFO, _('Welcome back %s!' % user))


def handle_logout(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, _('You have been logged out.'))
