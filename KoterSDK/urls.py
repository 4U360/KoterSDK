from django.urls import path, include
from .views import acme_webhook
from .rest.views import ContactViewSet
from rest_framework import routers

app_name = "koter-sdk"

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('webhook/<str:service>', acme_webhook, name="webhook"),
    path('datatables/', include('KoterSDK.ajax_datatables'), name="datatables"),
    path("api/", include(router.urls))
]
