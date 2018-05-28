from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer
from bookmarks.permissions import IsOwnerOnly
# Create your views here.


class UserBookmarksAPI(generics.ListCreateAPIView):
    """
    API to list and create bookmarks by a user.
    NOTE: This API is only accessible by authenticated users.
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        liu = self.request.user
        return liu.bookmarks.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookmarkDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API to retrieve/update/destroy a bookmark using its Primary Key.
    NOTE: This is only accessible by authenticated owners of bookmark.
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated, IsOwnerOnly)
    lookup_field = 'pk'  # being explicit here.

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
