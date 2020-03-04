from rest_framework import serializers
from stories.models import Story, STATUS_CHOICES, LICENSE_CHOICES

class StorySerializer(serializers.ModelSerializer):
    # tags = serializers.ListField(child=serializers.CharField(required=True))
    # admin_tags = serializers.ListField(child=serializers.CharField(required=True))
    # status = serializers.ChoiceField(choices=STATUS_CHOICES, required=True)
    # license = serializers.ChoiceField(choices=LICENSE_CHOICES, required=True)

    class Meta:
        model = Story
        fields = '__all__'  # serialize all fields
