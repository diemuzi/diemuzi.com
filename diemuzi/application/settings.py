"""
Settings
"""

from split_settings.tools import include
from split_settings.tools import optional

import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set Django Env
ENV = os.environ.get('DJANGO_ENV') or 'production'

include(
    # Components
    'components/secret.py',
    'components/apps.py',
    'components/middleware.py',
    'components/route.py',
    'components/database.py',
    'components/authenticate.py',
    'components/region.py',
    'components/cache.py',
    'components/session.py',
    'components/static.py',
    'components/message.py',
    'components/email.py',
    'components/https.py',
    'components/log.py',

    # Environments (development / production / testing)
    'environments/%s.py' % ENV,

    # Optional (application/local.py)
    optional('local.py')
)
