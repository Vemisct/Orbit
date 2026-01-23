from django import forms
from .models import Topic, Post

# Форма для створення посту
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введіть ваше повідомлення'}),
        }


# Форма для створення теми форуму
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }