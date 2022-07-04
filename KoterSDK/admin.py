from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Webhook, ExternalUser, Contact, AuditLog
from .modules.koter import Koter

@admin.register(Webhook)
class WebhookAdmin(VersionAdmin, admin.ModelAdmin):
    exclude = ("payload",)
    readonly_fields = ('_payload',)

    def _payload(self, obj: Webhook):
        try:
            koter = Koter()
            return koter.decode(obj.payload.get("data", ""))
        except Exception as er:
            return obj.payload


@admin.register(ExternalUser)
class ExternalUserAdmin(VersionAdmin, admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(VersionAdmin, admin.ModelAdmin):
    pass

@admin.register(AuditLog)
class AuditLogAdmin(VersionAdmin, admin.ModelAdmin):
    pass

