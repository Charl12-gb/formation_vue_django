from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializerAdd, TaskSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_project_task(request, project_id):
    # Exemple : Créer une nouvelle tâche pour un projet spécifique de l'utilisateur authentifié
    try:
        project = Projet.objects.get(id=project_id, user=request.user)
    except Projet.DoesNotExist:
        return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializerAdd, TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(project=project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def project_tasks(request, project_id):
    # Exemple : Récupérer toutes les tâches d'un projet spécifique de l'utilisateur authentifié
    try:
        project = Projet.objects.get(id=project_id, user=request.user)
    except Projet.DoesNotExist:
        return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)

    tasks = Tache.objects.filter(project=project)
    serializer = TaskSerializer, TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task(request, task_id):
    # Exemple : Récupérer une tâche spécifique de l'utilisateur authentifié par ID
    try:
        task = Tache.objects.get(id=task_id)
    except Tache.DoesNotExist:
        return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Assurez-vous que la tâche appartient à l'utilisateur authentifié
    if task.project.user != request.user:
        return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = TaskSerializer, TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)
