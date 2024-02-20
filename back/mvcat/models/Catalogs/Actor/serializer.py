from rest_framework import serializers
from .model import Actor

class ActorSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    age = serializers.CharField(max_length=150)
    name = serializers.CharField(max_length=150)
    birthday = serializers.DateField()

    class Meta:
        model = Actor
        fields = ["id", "name", "birthday", "age"]