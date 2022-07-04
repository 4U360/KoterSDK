from ..models import Contact
from rest_framework import serializers

# Serializers define the API representation.
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'