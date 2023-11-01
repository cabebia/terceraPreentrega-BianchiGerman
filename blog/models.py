from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250)
    postdate = models.DateField(auto_now_add=False)
    postContent = models.TextField()

    def __str__(self):
        return f'{self.id} - {self.title} - {self.subtitle}'
 