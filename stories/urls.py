from django.urls import path
from stories.views import ListCreateStories, StoryDetail, ListCreateStoryClaps, ListCreateComments, CommentDetail

urlpatterns = [
    path('', ListCreateStories.as_view(), name='list_create_stories'),
    path('<int:pk>', StoryDetail.as_view(), name='edit_story'),
    path('<int:pk>/claps', ListCreateStoryClaps.as_view(), name='story_claps'),
    path('<int:pk>/comments', ListCreateComments.as_view(), name='list_create_stories'),
    path('<int:story_pk>/comments/<int:comment_pk>', CommentDetail.as_view(), name='edit_comment')
]
