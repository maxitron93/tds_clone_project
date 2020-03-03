from rest_framework import serializers
from stories.models import Story, STATUS_CHOICES, LICENSE_CHOICES

class StorySerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField())
    admin_tags = serializers.ListField(child=serializers.CharField())
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    license = serializers.ChoiceField(choices=LICENSE_CHOICES)

    class Meta:
        model = Story
        fields = '__all__'  # serialize all fields
