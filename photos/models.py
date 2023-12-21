from django.db import models
from django.contrib.auth.models import User
from likephotos.models import Likephoto

class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return f"Photo by {self.id} at {self.caption}"

    @property
    def like_count(self):
        return self.likephotos.count()

    @property
    def comment_count(self):
        return self.photocomments.count()