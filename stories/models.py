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
    title = models.CharField(max_length=120)
    content = models.TextField()
    tags = ArrayField(models.CharField(max_length=120))
    admin_tags = ArrayField(models.CharField(max_length=120))
    num_claps = models.IntegerField()
    num_responses = models.IntegerField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='dft')
    seo_title = models.CharField(max_length=120)
    seo_description = models.TextField()
    license = models.CharField(max_length=3, choices=LICENSE_CHOICES, default='mit')
    free_link = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

