from django import forms
from .models import Announcement

class AnnForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'event', 'manual_date', 'description', 'conditions', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок оголошення'}),
            'event': forms.Select(attrs={'class': 'form-select'}),
            'manual_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Основний текст...'}),
            'conditions': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Додаткові умови (необов\'язково)'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'event': 'Прикріпити подію (необов\'язково)',
            'manual_date': 'Або вкажіть дату вручну'
        }