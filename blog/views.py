from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BlogPostForm
from .models import BlogPost
# Create your views here.

def v_index(request):
    last_4_post = BlogPost.objects.all().order_by('-id')[:4]

    return render(request, 'blog/index.html', {"posts": last_4_post})

class ListarPosts(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/index.html'

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        if title:
            posts = self.model.objects.filter(title__icontains=title)
            ...
        else:
            posts = self.model.objects.all().order_by('-id')[:4]
        return posts
    
    
def v_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.instance.userId = request.user
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 'blog/post.html', {'form': form})    

def v_about(request):

    return render(request, 'blog/about.html', {})

def v_contact(request):

    return render(request, 'blog/contact.html', {})

def v_samplepost(request, blogpostId):
    try:
        post = BlogPost.objects.get(id=blogpostId)
    except BlogPost.DoesNotExist:
        post = None

    return render(request, 'blog/samplepost.html', {"data": post})

class BorrarPost(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "blog/borrarpost.html"
    success_url = reverse_lazy("index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context

class EditPost(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = "blog/editpost.html"
    success_url = reverse_lazy("index")
    fields = ['title','subtitle','postContent']
