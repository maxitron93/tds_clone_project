from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from stories.models import Story
from stories.serializers import StorySerializer

def free_link_creator(title):
    return f'https://www.google.com/search?q={"%20".join(title.split(" "))}'

# Create your views here.
class ListStories(APIView):



    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StorySerializer(data=request.data)
        user_id = request.user.id
        serializer.initial_data['author'] = user_id # Add author
        serializer.initial_data['free_link'] = free_link_creator(serializer.initial_data['title']) # Add free_link
        serializer.initial_data['seo_title'] = serializer.initial_data['title'] # Add default seo_title
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
