from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_project(request):
    # Exemple : Créer un nouveau projet pour l'utilisateur authentifié
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_projects(request):
    # Exemple : Récupérer tous les projets de l'utilisateur authentifié
    projects = Projet.objects.filter(user=request.user)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def project(request, project_id):
    # Exemple : Récupérer un projet spécifique de l'utilisateur authentifié par ID
    try:
        project = Projet.objects.get(id=project_id, user=request.user)
    except Projet.DoesNotExist:
        return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)
