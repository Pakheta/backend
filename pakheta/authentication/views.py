from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SimpleAuthenticationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Try to authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is not None:
            # User is authenticated
            return Response({"authentication": True})
        else:
            # Invalid credentials
            return Response({"authentication": False}, status=status.HTTP_401_UNAUTHORIZED)
