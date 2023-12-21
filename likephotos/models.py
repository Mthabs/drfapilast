from django.db import models
from django.contrib.auth.models import User

class Likephoto(models.Model):
    photo = models.ForeignKey('photos.Photo', on_delete=models.CASCADE, related_name='likephotos')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['photo', 'owner']  

    def __str__(self):
        return f"Like by {self.owner} on Photo {self.photo}"