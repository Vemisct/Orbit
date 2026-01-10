from django.db import models

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

    name = models.CharField(max_length=100, verbose_name="Назва групи")
    code_number = models.CharField(max_length=20, unique=True, verbose_name="Кодовий номер")
    group_type = models.CharField(max_length=30, choices=GROUP_TYPES, default='tech', verbose_name="Тип групи")
    group_bio = models.TextField(blank=True, verbose_name="Опис групи")
    
    def __str__(self):
        return f"{self.name} ({self.code_number})"

    class Meta:
        verbose_name = "Група"
        verbose_name_plural = "Групи"

class Member(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    age = models.PositiveIntegerField(verbose_name="Вік")
    bio = models.TextField(blank=True, verbose_name="Біографія")
    
    group = models.ForeignKey(
        Group, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='members', 
        to_field='code_number',
        verbose_name="Група"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Учасник / Користувач"
        verbose_name_plural = "Учасники / Користувачі"