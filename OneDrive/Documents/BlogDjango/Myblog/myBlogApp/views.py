from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myBlogApp/post_list.html', {'posts': posts})
# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myBlogApp/post_details.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'myBlogApp/post_edit.html', {'form': form})