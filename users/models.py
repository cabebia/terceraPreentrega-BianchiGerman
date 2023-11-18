from django.db import models
from django.contrib.auth.models import User

class DatosExtra(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   nombre_completo = models.CharField(max_length=50)
   avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
   nivel = models.IntegerField(default=1)
   rango = models.CharField(max_length=20,default="Novatardo")