from rest_framework import serializers
from .models import Actor, Country
class ActorSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    age = serializers.CharField(max_length=150)
    name = serializers.CharField(max_length=150)
    birthday = serializers.DateField()
    class Meta:
        model = Actor
        fields = ["id", "name", "birthday", "age"]



class CountrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=50)
    class Meta:
        model = Country
        fields = ['id', 'name']