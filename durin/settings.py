from datetime import timedelta

from django.conf import settings
from django.test.signals import setting_changed
from rest_framework.settings import APISettings, api_settings

USER_SETTINGS = getattr(settings, "REST_DURIN", None)

DEFAULTS = {
    "DEFAULT_TOKEN_TTL": timedelta(days=1),
    "TOKEN_CHARACTER_LENGTH": 64,
    "USER_SERIALIZER": None,
    "AUTH_HEADER_PREFIX": "Token",
    "EXPIRY_DATETIME_FORMAT": api_settings.DATETIME_FORMAT,
    "TOKEN_CACHE_TIMEOUT": 60,
    "REFRESH_TOKEN_ON_USE": True
}

IMPORT_STRINGS = {
    "USER_SERIALIZER",
}

durin_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)


def reload_api_settings(*args, **kwargs):
    global durin_settings
    setting, value = kwargs["setting"], kwargs["value"]
    if setting == "REST_DURIN":
        durin_settings = APISettings(value, DEFAULTS, IMPORT_STRINGS)


setting_changed.connect(reload_api_settings)