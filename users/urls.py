from django.urls import path
from .views import v_login, v_register, v_index2, v_editar_perfil, CambiarPassword
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', v_index2, name = "index2"),
    path('login/', v_login, name="login"),
    path('register/', v_register, name="register"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('editar_perfil/', v_editar_perfil, name="editar_perfil"),
    path('cambiar_password', CambiarPassword.as_view(), name="cambiar_password"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

