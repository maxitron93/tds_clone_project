from django.urls import path
from stories.views import ListCreateStories, StoryDetail

urlpatterns = [
    path('', ListCreateStories.as_view(), name='list_create_stories'),
    path('<str:identifier>', StoryDetail.as_view(), name='edit_story'),
]