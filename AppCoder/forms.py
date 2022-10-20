from dataclasses import fields
from django import forms
from AppCoder.models import Series
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginFormulario(UserCreationForm):

    email = forms.EmailField()

class RegisterFormulario(UserCreationForm):

    email = forms.EmailField() 
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

class reseniaFormulario(forms.ModelForm):

    class Meta:

        model = Series
        fields = ['nombre', 'reseña', 'imagen']