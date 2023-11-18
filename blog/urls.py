from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import v_index, v_about, v_contact, v_post, v_samplepost, ListarPosts, EditPost
urlpatterns = [
    path('', v_index, name="index"),
    #path('index/', v_index, name="index"),
    path('index/', ListarPosts.as_view(), name="index"),
    path('post/', v_post, name="post"),
    path('about/', v_about, name="about"),
    path('contact/', v_contact, name="contact"),
    path('samplepost/<int:blogpostId>/', v_samplepost, name="samplepost"),
    path('editpost/<int:pk>', EditPost.as_view(), name="editpost"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
