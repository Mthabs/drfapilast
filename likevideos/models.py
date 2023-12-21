from django.db import models
from django.contrib.auth.models import User

class Likevideo(models.Model):
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE, related_name='likevideos')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['video', 'owner']  

    def __str__(self):
        return f"Like by {self.owner} on video {self.video}"
