import requests
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_external_user_model():
    """
    Return the External User model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.KOTER_EXTERNAL_USER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "KOTER_EXTERNAL_USER_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "KOTER_EXTERNAL_USER_MODEL refers to model '%s' that has not been installed"
            % settings.KOTER_EXTERNAL_USER_MODEL
        )


def has_new_version() -> bool:
    path = settings.BASE_DIR / "version"
    current_version = None
    if path.exists():
        current_version = path.open("r").read().strip()

