from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    GROUP_TYPES = [
        ('tech', 'Технології'), ('art', 'Мистецтво'), ('science', 'Наука'),
        ('social', 'Соціальність'), ('sport', 'Спорт'), ('music', 'Музика'),
        ('edu', 'Освіта'), ('eco', 'Екологія'), ('charity', 'Благодійництво'),
        ('game', 'Ігри'), ('photo', 'Фотографія'), ('cook', 'Кулінарія'),
        ('travel', 'Подорожі'), ('cinema', 'Кінематограф'), ('design', 'Дизайн'),
        ('fashion', 'Мода'), ('it', 'IT-розробка'), ('crypto', 'Криптовалюти'),
        ('history', 'Історія'), ('lit', 'Література'), ('health', 'Здоров\'я'),
        ('auto', 'Транспорт'), ('business', 'Бізнес'), ('space', 'Астрономія'),
    ]

    name = models.CharField(max_length=100)
    code_number = models.CharField(max_length=20, unique=True)
    group_type = models.CharField(max_length=30, choices=GROUP_TYPES, default='tech')
    group_bio = models.TextField(blank=True)
    capacity = models.PositiveIntegerField(default=10, verbose_name="Ліміт учасників")
    
    def __str__(self):
        return f"{self.name} ({self.members.count()}/{self.capacity})"

    @property
    def is_full(self):
        return self.members.count() >= self.capacity

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    bio = models.TextField(blank=True)
    group = models.ForeignKey(
        Group, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='members', 
        to_field='code_number'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"