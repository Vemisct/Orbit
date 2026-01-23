from django.db import models
from HeartBlock.models import Group, Member

class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100, verbose_name="Назва події")
    description = models.TextField(verbose_name="Опис", blank=True)
    date = models.DateTimeField(verbose_name="Дата та час")
    location = models.CharField(max_length=100, verbose_name="Місце проведення", default="Онлайн")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.group.name}"
    
    class Meta:
        ordering = ['date']