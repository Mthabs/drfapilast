from django.db import models
from django.contrib.auth.models import User

class Photocomment(models.Model):
    photo = models.ForeignKey('photos.Photo', on_delete=models.CASCADE, related_name='photocomments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return  f'{self.content}'
