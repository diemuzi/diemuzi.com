"""
Middleware
"""

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'locality.middleware.TimezoneMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware'
]
