from django.contrib import admin
from stories.models import Story, Tag, AdminTag, StoryClap, Response, ResponseClap

# Register your models here.
admin.site.register(Story)
admin.site.register(Tag)
admin.site.register(AdminTag)
admin.site.register(StoryClap)
admin.site.register(Response)
admin.site.register(ResponseClap)
