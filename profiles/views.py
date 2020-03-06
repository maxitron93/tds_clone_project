from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from profiles.models import Profile, Bookmark
from profiles.serializers import ProfileSerializer, BookmarkSerializer

class GetPatchProfile(APIView):

    def get(self, request):
        user = request.user
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = request.user
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListBookmarks(APIView):

    def get(self, request, status):
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user, status=status)
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data)

class GetPatchBookmark(APIView):

    def get(self, request, pk):
        bookmark = Bookmark.objects.get(pk=pk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    def patch(self, request, pk):
        bookmark = Bookmark.objects.get(pk=pk)
        serializer = BookmarkSerializer(bookmark, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


