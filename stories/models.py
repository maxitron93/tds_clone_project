from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

STATUS_CHOICES = [
        ('dft', 'Draft'),
        ('pub', 'Published')
    ]

LICENSE_CHOICES = [
        ('opn', 'Open Source'),
        ('mit', 'MIT License')
    ]

# Create your models here.
class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default='Untitled')
    content = models.TextField(default='<div></div>')
    tags = ArrayField(models.CharField(max_length=120, blank=True), default=list)
    admin_tags = ArrayField(models.CharField(max_length=120, blank=True), default=list)
    num_claps = models.IntegerField(default=0)
    num_responses = models.IntegerField(default=0)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='dft')
    seo_title = models.CharField(max_length=120, blank=True)
    seo_description = models.TextField(blank=True)
    license = models.CharField(max_length=3, choices=LICENSE_CHOICES, default='mit')
    free_link = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

class Tag(models.Model):
    title = models.CharField(max_length=120)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class AdminTag(models.Model):
    title = models.CharField(max_length=120)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class StoryClap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    body = models.TextField()
    num_claps = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ResponseClap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    num_claps = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
