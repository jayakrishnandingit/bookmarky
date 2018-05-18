from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer
# Create your views here.


class UserBookmarksAPI(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        liu = self.request.user
        return liu.bookmarks.all()


