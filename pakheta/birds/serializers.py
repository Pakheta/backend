from rest_framework import serializers
from .models import Bird, Birdset, Habitat


class HabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        field = "__all__"

class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = "__all__"


class BirdsetSerializer(serializers.ModelSerializer):
    birdset = BirdSerializer()

    class Meta:
        model = Birdset
        field = "__all__"

