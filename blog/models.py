from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class BlogPost(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250)
    postdate = models.DateField(auto_now_add=True)
    postContent = RichTextField()

    def __str__(self):
        return f'{self.id} - {self.title} - {self.subtitle}'
 