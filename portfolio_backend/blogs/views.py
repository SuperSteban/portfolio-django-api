from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Blog
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, status, permissions, viewsets
from .serializer import BlogSerializer

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Blog.objects.all().order_by('created_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user) 
        else:
            print(serializer.errors)

class BlogListViewPublic(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('created_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]

