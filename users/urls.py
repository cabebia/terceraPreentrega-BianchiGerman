from django.urls import path
from .views import v_login, v_register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', v_login, name="login"),
    path('register/', v_register, name="register"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
