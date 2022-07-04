from ..models import Contact
from rest_framework import viewsets
from .serializers import ContactSerializer
from ..permissions import IsValidRequest

# Serializers define the API representation.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.filter(has_optout=False)
    serializer_class = ContactSerializer
    permission_classes = [IsValidRequest]

