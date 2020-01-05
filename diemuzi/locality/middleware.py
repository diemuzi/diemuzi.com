import pytz

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddleware(MiddlewareMixin):
    """
    Timezone Middleware
    """

    @staticmethod
    def process_request(request):
        tzname = request.session.get('django_timezone')

        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
