"""
Language / i18N Support
"""

import os

from application.settings import BASE_DIR

# Internationalization
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'region/language')
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
