from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# ... (Group model залишається без змін) ...

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
    GENDER_CHOICES = [
        ('none', 'Не визначено'),
        ('male', 'Чоловік'),
        ('female', 'Жінка'),
    ]
    
    # Вибір обводки (зберігаємо як CSS клас або ID)
    BORDER_CHOICES = [
        ('none', 'Немає'),
        ('neon', 'Неон'),
        ('gold', 'Золото'),
        ('fire', 'Вогонь'),
    ]

    # Вибір фону (зберігаємо як CSS клас або ID)
    BG_CHOICES = [
        ('default', 'Стандартний'),
        ('space', 'Космос'),
        ('sunset', 'Захід сонця'),
        ('cyber', 'Кіберпанк'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='member')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=18)
    bio = models.TextField(blank=True, default="")
    status = models.CharField(max_length=100, blank=True, default="")
    avatar = models.ImageField(upload_to='StaticBlock/ImgCell/Avatars/', null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    
    # Нові поля
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='none')
    email = models.EmailField(unique=True, null=True, blank=True) # Для верифікації
    
    # Orbit Plus Visuals
    avatar_border = models.CharField(max_length=50, choices=BORDER_CHOICES, default='none', blank=True)
    profile_bg = models.CharField(max_length=50, choices=BG_CHOICES, default='default', blank=True)
    
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

# ... (GroupComment залишається без змін) ...
class GroupComment(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author} on {self.group}"
    
    @property
    def can_be_deleted(self):
        return timezone.now() < self.created_at + timezone.timedelta(minutes=10)