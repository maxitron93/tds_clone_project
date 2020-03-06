from django.db import models
from django.contrib.auth.models import User
from stories.models import Story
from django.db.models.signals import post_save

BOOKMARK_CHOICES = [
        ('read', 'Read'),
        ('saved', 'Saved'),
        ('archived', 'Archived')
    ]

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    receive_emails = models.BooleanField(default=True)
    receive_notifications = models.BooleanField(default=True)
    receive_updates = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

post_save.connect(create_profile, User)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=BOOKMARK_CHOICES, default='read')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followings')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

