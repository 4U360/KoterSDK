from django.conf import settings
from rest_framework.permissions import BasePermission
from secrets import compare_digest
from ipware import get_client_ip
from .models import AuditLog


class IsValidRequest(BasePermission):

    def has_permission(self, request, view, user=None):
        given_token = request.headers.get(settings.KOTER_SECRET_HEADER, "")
        client_ip, _ = get_client_ip(request)
        in_whitelist = client_ip in settings.KOTER_IP_WHITELIST
        success = all(
            [compare_digest(given_token, settings.KOTER_INTEGRATION_ID),
             in_whitelist])

        AuditLog.objects.create(
            ip_address=client_ip,
            location=request.build_absolute_uri(),
            message=f"""External client is requesting permission to access the resource.\nPermission status: {'granted' if success else 'denied'}"""
        )
        return success
