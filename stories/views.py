from rest_framework.views import APIView
from rest_framework.response import Response
from stories.models import Story
from stories.serializers import StorySerializer

# Create your views here.
class ListStories(APIView):

    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

