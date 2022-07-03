from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class KotersdkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'KoterSDK'
    verbose_name = _("Koter SDK")
