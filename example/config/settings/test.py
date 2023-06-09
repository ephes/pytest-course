"""
Django settings for locnus project in test mode

Make sure to override `DJANGO_SETTINGS_MODULE` environment variable to use this file.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from .base import *  # noqa

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# Make tests faster by using a noop hasher
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
