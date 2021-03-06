"""bookmarky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path

from rest_framework.schemas import get_schema_view

from bookmarks import views as bookmarks_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', get_schema_view()),
    path('api/v1.0/auth/', include('rest_auth.urls')),
    path('api/v1.0/auth/registration/', include('rest_auth.registration.urls')),

    path('api/v1.0/me/bookmarks/', bookmarks_views.UserBookmarksAPI.as_view(), name='mybookmarks'),
    path('api/v1.0/bookmarks/<int:id>/', bookmarks_views.BookmarkDetailsAPI.as_view(), name='bookmark'),
]
