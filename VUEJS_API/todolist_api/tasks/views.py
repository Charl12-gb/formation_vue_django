from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated 
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import UserSerializer 


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None:
            return Response({'message': 'Please provide an username number.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist: 
            return Response({'message': 'Incorrect username or password!'}, status=status.HTTP_400_BAD_REQUEST)

        # Utilisez la fonction d'authentification Django pour vérifier les informations d'identification
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'message': 'Incorrect username or password!'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)

        response = {
            'message': 'Welcome! Successfully connected.',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': self.serializer_class(user).data
        }

        return Response(response, status=status.HTTP_200_OK)

class UserTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = request.user
            return Response({
                'refresh': str(response.data.get('refresh')),
                'access': str(response.data.get('access')),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            })
        return response

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
