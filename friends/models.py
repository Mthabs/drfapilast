from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    owner = models.ForeignKey(User, related_name='friendships', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'friend']

    def __str__(self):
        return f'{self.owner} is friends with {self.friend}'
