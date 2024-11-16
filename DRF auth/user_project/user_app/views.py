from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterSerializer,UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserRegistration(APIView):
    def get(self,request):
        serializer = RegisterSerializer()
        return Response(serializer.data)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({ 'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def get(self,request):
        serializer = UserSerializer()
        return Response(serializer.data)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"message":'Please enter the correct username and password THank YOu!'})

        elif user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': f'Successfully logged in as {request.user}.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response(f'You r LOgin as {request.user}.For logout plz send a Post request and add a Token in Headers ')

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({'message': f"Successfully logged out {request.user}"})