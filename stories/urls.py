from django.urls import path
from .views import ListStories

urlpatterns = [
    path('', ListStories.as_view(), name='stories_list')
]