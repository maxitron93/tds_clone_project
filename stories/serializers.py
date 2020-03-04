from rest_framework import serializers
from stories.models import Story, STATUS_CHOICES, LICENSE_CHOICES

class StorySerializer(serializers.ModelSerializer):
    free_link = serializers.SerializerMethodField('return_free_link')

    # This is how to return a field that's not in the database
    def return_free_link(self, story):
        return f'https://google.com/search?q={"%20".join(story.title.split(" "))}'

    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ['identifier', 'created_at', 'updated_at', 'author', 'num_claps', 'num_responses']

