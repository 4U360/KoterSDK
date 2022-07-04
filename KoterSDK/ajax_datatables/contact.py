from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from ajax_datatable.views import AjaxDatatableView
from secrets import compare_digest
from ..models import Contact, ExternalUser


class ContactDatatableView(AjaxDatatableView):
    model = Contact
    title = _("Contacts")
    initial_order = [["first_name", "asc"], ['last_name', 'asc']]
    length_menu = [[10, 20, 50, 100], [10, 20, 50, 100]]

    column_defs = [
        {'name': 'id', 'visible': False},
        {'name': 'first_name', 'visible': True, 'title': _('First Name')},
        {'name': 'last_name', 'visible': True, 'title': _('Last Name')},
        {'name': 'phone', 'visible': True, 'title': _('Phone')},
        {'name': 'created', 'visible': True, 'title': _('Created')}
    ]

    def get_initial_queryset(self, request=None):
        if not getattr(request, 'REQUEST', None):
            request.REQUEST = request.GET if request.method == 'GET' else request.POST

        given_token = request.headers.get(settings.KOTER_SECRET_HEADER, "")

        if not compare_digest(given_token, settings.KOTER_INTEGRATION_ID):
            raise PermissionDenied

        return super(ContactDatatableView, self).get_initial_queryset(request)
