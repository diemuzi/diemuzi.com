"""
Authentication
"""

# Authentication Model
AUTH_USER_MODEL = 'login.Account'

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'login.backends.AuthBackend'
]

# Password Hashers
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher'
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 5
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    }
]

# Login / Redirect URL's
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

# Logout / Redirect URL's
LOGOUT_URL = '/login/logout'
LOGOUT_REDIRECT_URL = LOGIN_URL

# Exclude Group Permissions from apps
EXCLUDE_GROUP_APPS = [
    'auth',
    'contenttypes',
    'django_celery_results',
    'database',
    'sessions',
    'sites'
]

# Default Group Permissions
GROUP_PERMISSIONS = [
    'blog.add_comment',
    'blog.change_comment',
    'blog.delete_comment',
    'blog.view_comment',
    'cook.add_comment',
    'cook.change_comment',
    'cook.delete_comment',
    'cook.view_comment',
    'login.change_account',
    'login.change_password',
    'login.delete_account',
    'login.view_accesslog',
    'login.view_account',
    'login.view_password'
]
