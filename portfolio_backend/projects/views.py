from django.shortcuts import render
from .models import Project
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, status, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import ProjectSerializer

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Project.objects.all().order_by('created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user) 
        else:
            print(serializer.errors)

    
class ProjectListViewPublic(generics.ListAPIView):
    queryset = Project.objects.all().order_by('created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


class ProjectFilterListViewPublic(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pinned']

       
        