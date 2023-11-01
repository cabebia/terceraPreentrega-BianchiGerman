from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
# Create your views here.

def v_index(request):
    last_4_post = BlogPost.objects.all().order_by('-id')[:4]

    return render(request, 'blog/index.html', {"posts": last_4_post})

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
