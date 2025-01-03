from rest_framework import serializers
from .models import Bird, Birdset


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = "__all__"


class BirdsetSerializer(serializers.ModelSerializer):
    birdset = BirdSerializer()

    class Meta:
        model = Birdset
        field = "__all__"

