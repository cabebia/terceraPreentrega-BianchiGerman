from django.contrib import admin
from .models import BlogPost
from users.models import DatosExtra
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(DatosExtra)