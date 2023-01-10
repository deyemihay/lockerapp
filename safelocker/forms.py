from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import UserLocker
from django.contrib.auth.models import User


class LockerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['site_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'site name',
        })
        self.fields['site_url'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'site url',
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'username',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'password',
        })

    class Meta:
        model = UserLocker
        fields = ('site_name', 'site_url', 'username', 'email', 'password')


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'first name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'last name',
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'username',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'confirm password',
        })

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
