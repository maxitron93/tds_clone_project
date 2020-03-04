from django.urls import path
from stories.views import ListCreateStories

urlpatterns = [
    path('', ListCreateStories.as_view(), name='list_create_stories'),
]