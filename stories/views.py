from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from stories.models import Story
from stories.serializers import StoriesSerializer

class ListCreateStories(APIView):

    def get(self, request):
        stories = Story.objects.all()
        serializer = StoriesSerializer(stories, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Serialize the incoming data
        serializer = StoriesSerializer(data=request.data)

        # Add user to the serialized data
        user_id = request.user.id
        serializer.initial_data['author'] = user_id # Add author

        # If everything is valid, create the story
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
