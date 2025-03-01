"""
URL configuration for portfolio_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from users.views import CreateUserView
from projects.views import ProjectViewSet, ProjectListViewPublic, ProjectFilterListViewPublic
from search.views import GlobalSearchView
from blogs.views import BlogViewSet 
from blogs.views import BlogListViewPublic
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'blogs', BlogViewSet, basename='blogs')






urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api/search/', GlobalSearchView.as_view(), name='buscar'),
    path("api/users/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api/public/blogs/", BlogListViewPublic.as_view(), name='blogs_public'),
    path("api/public/projects/", ProjectListViewPublic.as_view(), name='projects_public'),
    path("api/public/projects-filter/", ProjectFilterListViewPublic.as_view(), name='projects_public_filter'),


    path("api-auth", include("rest_framework.urls"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
