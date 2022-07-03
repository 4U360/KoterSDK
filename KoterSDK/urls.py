from django.urls import path
from .views import acme_webhook

app_name = "koter-sdk"

urlpatterns = [
    path('webhook/<str:service>', acme_webhook, name="webhook"),
]
