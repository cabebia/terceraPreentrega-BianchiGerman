from django.urls import path
from .views import v_index, v_about, v_contact, v_post, v_samplepost, add_3_users
urlpatterns = [
    path('', v_index, name="index"),
    path('index/', v_index, name="index"),
    path('post/', v_post, name="post"),
    path('about/', v_about, name="about"),
    path('contact/', v_contact, name="contact"),
    path('samplepost/<int:blogpostId>/', v_samplepost, name="samplepost"),
    path('add_3_users', add_3_users),
]
