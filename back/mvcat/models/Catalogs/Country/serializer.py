from rest_framework import serializers
from .model import Country

class CountrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=50)
    class Meta:
        model = Country
        fields = ['id', 'name']