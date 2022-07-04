from .contact import ContactDatatableView
from django.urls import path

urlpatterns = [
    path('contact', ContactDatatableView.as_view(), name="contact")
]