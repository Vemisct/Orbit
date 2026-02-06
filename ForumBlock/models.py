from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.created_by.username} in {self.topic.title}"