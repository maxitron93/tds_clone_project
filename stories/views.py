from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from stories.models import Story
from stories.serializers import StorySerializer

class ListCreateStories(APIView):

    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    # Only empty stories can be created
    def post(self, request):

        # Get user and unique identifier
        user = request.user
        identifier = 'placeholder2'

        # Create new story
        new_story = Story(author = user, identifier = identifier)
        new_story.save()

        # Return the identifier
        return Response({'identifier': identifier}, status=status.HTTP_201_CREATED)

class StoryDetail(APIView):

    def get_object(self, identifier):
        object = get_object_or_404(Story, identifier=identifier)
        return object

    def get(self, request, identifier):
        story = self.get_object(identifier)
        serializer = StorySerializer(story)
        return Response(serializer.data)

    def patch(self, request, identifier):
        story = self.get_object(identifier)
        serializer = StorySerializer(story, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, identifier):
        story = self.get_object(identifier)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
