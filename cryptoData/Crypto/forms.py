from django import forms
from .models import CryptoProject
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task

class CryptoProjectForm(forms.ModelForm):
    class Meta:
        model = CryptoProject
        fields = ['name', 'website', 'contact_info', 'market_cap', 'volume']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'contact_info': forms.EmailInput(attrs={'class': 'form-control'}),
            'market_cap': forms.NumberInput(attrs={'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'deadline', 'priority', 'status', 'intern']