from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.permissions import AllowAny
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response
from django.db.models import Q
from projects.models import Project
from blogs.models import Blog
from projects.serializer import ProjectSerializer
from blogs.serializer import BlogSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class GlobalSearchView(generics.ListAPIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    pagination_class = CursorPagination
    def get(self, request, *args, **kwargs):
        query = request.GET.get('', '')
        if not query:
            return Response({'error': 'Debes proporcionar un término de búsqueda'}, status=status.HTTP_400_BAD_REQUEST)


        # Buscar con regex en múltiples modelos
        projects = Project.objects.filter(Q(title__iregex=query) | Q(description__iregex=query))
        blogs = Blog.objects.filter(Q(title__iregex=query) | Q(description__iregex=query))

        # Serializar los resultados
        projects_serializer = ProjectSerializer(projects, many=True).data
        blogs_serializer = BlogSerializer(blogs, many=True).data

        return Response({
            'projects': projects_serializer,
            'blogs': blogs_serializer,
        }, status=status.HTTP_200_OK)
      

        

