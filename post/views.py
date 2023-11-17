from django.shortcuts import render, redirect
from .models import Post
from django.http import Http404
from .forms import PostForm, PostUpdateForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def posts(request):
    try:
        posts = Post.objects.all().order_by('-created')
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)

def detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    context = {
        'post': post
    }
    return render(request, 'detail.html', context)

# ------------

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:posts')
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts:posts')

    context = {
        'post': post
    }
    return render(request, 'delete.html', context)


def post_update(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:posts')
    else:
        form = PostUpdateForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'update.html', context)