from django.db import models
from django.contrib.auth.models import User

class Videocomment(models.Model):
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE, related_name='videocomments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return  f'{self.content}' 