from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Bird, Birdset
from .serializers import BirdSerializer, BirdsetSerializer
import requests
from django.db import connection

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

class BirdPredictionView(APIView):
    def post(self, request):
        audio_file = request.FILES.get('audio')
        
        if not audio_file:
            return Response({"error": "No audio file provided"}, status=status.HTTP_400_BAD_REQUEST)

        response = requests.post(
            'https://mryeti-featherfindapi.hf.space/predict/',
            files={'audio_file': audio_file}
        )

        if response.status_code != 200:
            return Response({"error": "Failed to get prediction from external API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        prediction = response.json()

        return Response(prediction, status=status.HTTP_200_OK)