from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category

def blog_list(request):
    posts = Post.objects.filter(status='published').order_by('-created_on')
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page = request.GET.get('page')
    posts_page = paginator.get_page(page)

    return render(request, 'blog/blog_list.html', {
        'posts': posts_page,
        'title': 'Blog | Rescue Me'
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'title': f'{post.title} | Rescue Me'
    })

# This is the function that's missing and causing the error
def index(request):
    # Redirect to blog_list or show featured posts
    posts = Post.objects.filter(status='published').order_by('-created_on')[:3]
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'title': 'Blog | Rescue Me',
        'is_index': True
    })