from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        labels = {
            'username': 'Usuario',
            'password1': 'Contraseña',
            'password2': 'Repetir contraseña',
        }