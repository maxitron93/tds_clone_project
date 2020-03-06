from rest_framework.serializers import ModelSerializer
from profiles.models import Profile

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['is_admin', 'user']
