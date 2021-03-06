import uuid as uuid
from django.db import models
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from mirage.fields import EncryptedEmailField, EncryptedCharField, EncryptedURLField, EncryptedTextField, \
    EncryptedJSONField
from .fields import EncryptedPhonenumberField, EncryptedCPFFIeld, EncryptedIPAddressField
from django.utils.translation import gettext_lazy as _
from tagulous.models import TagField
from versionfield import VersionField


class ExternalUser(TimeStampedModel, ActivatorModel):
    first_name = models.CharField(max_length=120, blank=True, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=120, blank=True, verbose_name=_("Last Name"))
    email = EncryptedEmailField(blank=True, verbose_name=_("Email"))
    fingerprint = EncryptedTextField(blank=True, verbose_name=_("Fingerprint"))
    cpf = EncryptedCPFFIeld(blank=True, masked=True, db_index=True, verbose_name=_("CPF"))

    class Meta:
        verbose_name = _("External User")
        verbose_name_plural = _("External Users")


class AuditLog(TimeStampedModel):
    ip_address = EncryptedIPAddressField(blank=True, null=True, verbose_name=_("IP Address"))
    location = models.URLField(blank=True, null=True, verbose_name=_("URL Location"))
    message = EncryptedTextField(verbose_name=_("Message"))
    external_user = models.ForeignKey(ExternalUser, db_index=True, on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name=_("External User"))


class Webhook(TimeStampedModel):
    service = models.CharField(max_length=120, db_index=True, verbose_name=_("Service"))
    payload = EncryptedJSONField(default=None, null=True, verbose_name=_("Payload"))

    def __str__(self):
        return f'Webhook ({self.service if self.service else "No-Service"}) object ({self.pk})'

    class Meta:
        indexes = [
            models.Index(fields=['created'])
        ]


class Contact(TimeStampedModel, ActivatorModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    fingerpint = EncryptedTextField(max_length=512, blank=True, verbose_name=_("Fingerprint"))
    first_name = EncryptedCharField(max_length=120, blank=True, verbose_name=_("First Name"))
    last_name = EncryptedCharField(max_length=120, blank=True, verbose_name=_("Last Name"))
    phone = EncryptedPhonenumberField(db_index=True, verbose_name=_("Phone"))
    google_id = EncryptedCharField(max_length=80, blank=True, verbose_name=_("Google ID"))
    has_optin = models.BooleanField(default=False, verbose_name=_("Has Optin"))
    optin_origin = EncryptedURLField(verbose_name=_("Source URL"))
    optin_additional_info = EncryptedTextField(verbose_name=_("Additional information about optin"), blank=True)
    has_optout = models.BooleanField(default=False, verbose_name=_("Has optout"))
    optout_origin = EncryptedURLField(blank=True, verbose_name=_("Optout Source URL"))
    optout_additional_info = EncryptedTextField(verbose_name=_("Additional opt-out information"), blank=True)
    mcp_by_phone = EncryptedTextField(blank=True, null=True, verbose_name=_("Marketing Communications Permission"))
    date_mcp = models.DateTimeField(verbose_name=_("Date MCP"))
    pep = models.CharField(max_length=560, verbose_name=_("Publicly Exposed (Brazil)"))
    tags = TagField(blank=True, verbose_name=_("Tags"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
