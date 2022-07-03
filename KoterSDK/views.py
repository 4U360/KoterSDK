import datetime as dt
import json
from secrets import compare_digest

from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Webhook
from .signals import pre_receive_hook, post_receive_hook


@csrf_exempt
@require_POST
@non_atomic_requests
def acme_webhook(request, service):
    given_token = request.headers.get(settings.KOTER_SECRET_HEADER, "")

    if not compare_digest(given_token, settings.KOTER_INTEGRATION_ID):
        return HttpResponseForbidden(
            "Incorrect token in Koter-Webhook-Token header.",
            content_type="text/plain",
        )

    pre_receive_hook.send(Webhook.__class__, request=request)

    if settings.KOTER_DELETE_OLD_HOOKS:
        Webhook.objects.filter(
            created__lte=timezone.now() - dt.timedelta(days=settings.KOTER_DELETE_HOOKS_IN_N_DAYS)
        ).delete()

    payload = json.loads(request.body)
    instance = Webhook.objects.create(
        service=service,
        payload=payload
    )
    post_receive_hook.send(Webhook.__class__, instance=instance)
    return HttpResponse(status=200, content_type="text/plain")
