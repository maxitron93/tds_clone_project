from rest_framework import serializers
from stories.models import Story, STATUS_CHOICES, LICENSE_CHOICES, StoryClap, Comment

class StorySerializer(serializers.ModelSerializer):
    free_link = serializers.SerializerMethodField('return_free_link')

    # This is how to return a field that's not in the database
    def return_free_link(self, story):
        return f'https://google.com/search?q={"%20".join(story.title.split(" "))}'

    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ['author', 'num_claps', 'num_responses', 'created_at', 'updated_at']

class StoryClapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryClap
        fields = '__all__'
        read_only_fields = ['user', 'story']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'