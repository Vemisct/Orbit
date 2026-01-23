from django import forms
from .models import *

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'age', 'bio', 'group']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ім\'я'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше прізвище'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Вік'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Біографія'}),
        }
        labels = {
            'first_name': 'Ім\'я',
            'last_name': 'Прізвище',
            'age': 'Вік',
            'bio': 'Біографія',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = GroupComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Напишіть щось про цю групу...'
            }),
        }
        labels = {
            'content': ''
        }