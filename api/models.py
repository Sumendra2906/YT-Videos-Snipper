from django.db import models

class VideosInfo(models.Model):
    video_id = models.CharField(max_length=200,  blank=False, null=False, unique=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    published_on = models.DateTimeField()
    thumbnail_default_url = models.URLField()
    channel_id = models.CharField(max_length=500, blank=False, null=False)
    channel_title = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)