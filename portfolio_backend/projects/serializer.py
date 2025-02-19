from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description','img', 'created_at', 'author', 'pinned']
        extra_kwargs = {"author": {"read_only": True}}
    
