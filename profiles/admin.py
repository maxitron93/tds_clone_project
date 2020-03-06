from django.contrib import admin
from profiles.models import Profile, Bookmark, Following

# Register your models here.
admin.site.register(Profile)
admin.site.register(Bookmark)
admin.site.register(Following)
