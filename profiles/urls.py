from django.urls import path
from profiles.views import GetPatchProfile, ListBookmarks, GetPatchBookmark, CreateBookmark

urlpatterns = [
    path('', GetPatchProfile.as_view(), name='get_patch_profile'),
    path('create_bookmark/<int:pk>', CreateBookmark.as_view(), name='create_bookmark'),
    path('bookmarks/<str:status>', ListBookmarks.as_view(), name='list_bookmarks'),
    path('bookmark/<int:pk>', GetPatchBookmark.as_view(), name='get_patch_bookmarks')
]