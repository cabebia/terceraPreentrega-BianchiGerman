from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class EdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email', required=False)
    nombre_completo = forms.CharField(max_length=50,label='Cambiar nombre', required=False)
    avatar = forms.ImageField(label="Cambiar avatar:",required=False)
    nivel = None
    rango = None
    
    class Meta:
        model = User
        fields = ['email', 'nombre_completo', 'avatar']