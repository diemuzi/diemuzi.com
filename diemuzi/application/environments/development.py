"""
Development Override Settings
"""

from application.components.apps import INSTALLED_APPS
from application.components.middleware import MIDDLEWARE

# Debug
DEBUG = True

# Allowed Hosts
ALLOWED_HOSTS = []

# Site ID
SITE_ID = 1

# Installed Applications
INSTALLED_APPS.append('debug_toolbar')
INSTALLED_APPS.append('django_extensions')

# Middleware
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# Django Debug Toolbar
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel'
]

DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'application.settings.show_toolbar'
}


def show_toolbar(request):
    return request
