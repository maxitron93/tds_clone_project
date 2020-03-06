from django.urls import path
from profiles.views import GetPatchProfile, ListBookmarks, GetPatchBookmark

urlpatterns = [
    path('', GetPatchProfile.as_view(), name='get_patch_profile'),
    path('bookmarks/<str:status>', ListBookmarks.as_view(), name='get_patch_profile'),
    path('bookmark/<int:pk>', GetPatchBookmark.as_view(), name='get_patch_profile'),
]