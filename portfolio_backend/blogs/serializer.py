from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created_at', 'author','img',]
        extra_kwargs = {'author': {'read_only': True}}