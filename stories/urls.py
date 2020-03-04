from django.urls import path
from stories.views import ListCreateStories, StoryDetail, ListCreateStoryClaps

urlpatterns = [
    path('', ListCreateStories.as_view(), name='list_create_stories'),
    path('<int:pk>', StoryDetail.as_view(), name='edit_story'),
    path('<int:pk>/claps', ListCreateStoryClaps.as_view(), name='edit_story'),
]