from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_list(request):
    # Only show published posts, ordered by creation date
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def post_detail(request, slug):  # Changed from pk to slug
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'blog/post_detail.html', {'post': post})