from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class TaskSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
