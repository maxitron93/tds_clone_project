from django.urls import path
from profiles.views import GetPatchProfile

urlpatterns = [
    path('', GetPatchProfile.as_view(), name='get_patch_profile'),
]