"""
Static Content
"""

import os

from application.settings import BASE_DIR

# Media files (user uploaded images)
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static files (CSS, Fonts, Images, JavaScript)
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Compressor Support
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]

COMPRESS_ENABLED = True

COMPRESS_OFFLINE = True

COMPRESS_URL = STATIC_URL

COMPRESS_ROOT = STATIC_ROOT

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]

# See components/cache.py
COMPRESS_CACHE_BACKEND = 'default'
