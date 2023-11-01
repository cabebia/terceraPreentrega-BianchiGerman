from django import forms
from .models import BlogPost  # Asegúrate de que estás importando tu modelo BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'postContent']
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'postContent': 'Empieze a escribir su idea aca:',
        }
