"""
Applications
"""

# Django Applications
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles'
]

# Third-Party Applications
INSTALLED_APPS.extend([
    'django_cleanup.apps.CleanupConfig',
    'compressor',
    'widget_tweaks'
])

# Contrib Applications
INSTALLED_APPS.extend([
    'comment.apps.CommentConfig',
    'form.apps.FormConfig',
    'locality.apps.LocalityConfig',
    'template.apps.TemplateConfig',
])

# Project Applications
INSTALLED_APPS.extend([
    'about.apps.AboutConfig',
    'asset.apps.AssetConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'cook.apps.CookConfig',
    'home.apps.HomeConfig',
    'login.apps.LoginConfig',
    'member.apps.MemberConfig',
    'photo.apps.PhotoConfig'
])
