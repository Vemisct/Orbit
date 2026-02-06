from django.db import models
from HeartBlock.models import Group

class Announcement(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=200, verbose_name="Назва")
    event = models.ForeignKey('EventsBlock.Event', on_delete=models.SET_NULL, null=True, blank=True, related_name='ann_linked', verbose_name="Пов'язана подія")
    manual_date = models.DateTimeField(verbose_name="Дата/Час (вручну)", null=True, blank=True)
    description = models.TextField(verbose_name="Основний текст")
    conditions = models.TextField(verbose_name="Умови/Деталі", blank=True, null=True)
    image = models.ImageField(upload_to='StaticBlock/ImgCell/Announcements/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.group.name}"