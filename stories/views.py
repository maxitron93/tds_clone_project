from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from stories.models import Story, StoryClap, Comment, CommentClap
from stories.serializers import StorySerializer, StoryClapsSerializer, CommentSerializer, CommentClapsSerializer

class ListCreateStories(APIView):

    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    # Only empty stories can be created
    def post(self, request):

        # Get user and unique identifier
        user = request.user

        # Create new story
        new_story = Story(author = user)
        new_story.save()

        # Serialize the story
        serializer = StorySerializer(new_story)

        # Return the story
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class StoryDetail(APIView):

    def get_object(self, pk):
        object = get_object_or_404(Story, pk=pk)
        return object

    def get(self, request, pk):
        story = self.get_object(pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)

    def patch(self, request, pk):
        story = self.get_object(pk)
        serializer = StorySerializer(story, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        story = self.get_object(pk)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListCreateStoryClaps(APIView):

    def get(self, request, pk):
        claps = StoryClap.objects.filter(story=pk)
        serializer = StoryClapsSerializer(claps, many=True)
        return Response(serializer.data)


    def post(self, request, pk):

        # Get clap information
        user = request.user
        story = Story.objects.get(pk=pk)

        # Create clap
        clap = StoryClap(user = user, story = story)
        clap.save()

        return Response({'response': 'clap recorded'})

class ListCreateComments(APIView):

    def get(self, request, pk):
        comments = Comment.objects.filter(story=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        user = request.user.id
        story = pk
        body = request.data['body']
        new_comment = {'user': user, 'story': story, 'body': body}
        serializer = CommentSerializer(data=new_comment)

        if serializer.is_valid():
            serializer.save()  # Triggers the update method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self, pk):
        object = get_object_or_404(Comment, pk=pk)
        return object

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, pk):
        comment = self.get_object(pk)
        data = {'body': request.data['body']}
        serializer = CommentSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCreateCommentClaps(APIView):

    def get(self, request, pk):
        claps = CommentClap.objects.filter(comment=pk)
        serializer = CommentClapsSerializer(claps, many=True)
        return Response(serializer.data)

    def post(self, request, pk):

        # Get clap information
        user = request.user
        story = Comment.objects.get(pk=pk)

        # Create clap
        clap = CommentClap(user=user, comment=story)
        clap.save()

        return Response({'response': 'clap recorded'})
