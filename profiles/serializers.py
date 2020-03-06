from rest_framework.serializers import ModelSerializer
from profiles.models import Profile, Bookmark

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['is_admin', 'user']

class BookmarkSerializer(ModelSerializer):

    class Meta:
        model = Bookmark
        fields = '__all__'