from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву події'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Детальний опис'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}), # Браузерний календар
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Online / Адреса'}),
        }
        labels = {
            'title': 'Назва події',
            'description': 'Опис',
            'date': 'Дата та час',
            'location': 'Місце проведення',
        }