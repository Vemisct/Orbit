from django import forms
from .models import *

class MemberEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'first_name', 'last_name', 'age', 'bio', 
            'status', 'gender', 'email', 'avatar', 'avatar_border', 'profile_bg'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ім\'я'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Прізвище'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш статус...'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Розкажіть про себе...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com', 'readonly': 'readonly'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'id': 'avatar-input'}),
            
            # Приховані поля, які заповнюються JavaScript-ом при кліку на карусель
            'avatar_border': forms.HiddenInput(),
            'profile_bg': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.member = kwargs.get('instance')
        super(MemberEditForm, self).__init__(*args, **kwargs)
        if not self.member.email:
            self.fields['email'].widget.attrs.pop('readonly', None)

    def clean_avatar_border(self):
        """Перевірка: чи має право юзер ставити обводку"""
        border = self.cleaned_data.get('avatar_border')
        if border != 'none' and not self.member.is_premium:
            return 'none'
        return border
    
    def clean_profile_bg(self):
        """Захист фону профілю"""
        bg = self.cleaned_data.get('profile_bg')
        if bg != 'default' and not self.member.is_premium:
            return 'default'
        return bg

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