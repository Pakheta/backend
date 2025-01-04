from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Bird, Birdset
from .serializers import BirdSerializer, BirdsetSerializer

class BirdListView(APIView):
    def get(self, request):
        birds = Bird.objects.all()
        serializer = BirdSerializer(birds, many=True)
        return Response(serializer.data)

class BirdView(APIView):
    def get(self, request, bird_id):
        bird = get_object_or_404(Bird, id=bird_id)
        serializer = BirdSerializer(bird)
        return Response(serializer.data)

class BirdsetView(APIView):
    def get(self, request, bird_id):
        bird = get_object_or_404(Bird, id=bird_id)
        birds = Birdset.objects.filter(bird=bird)
        serializer = BirdsetSerializer(birds, many=True)
        return Response(serializer.data)