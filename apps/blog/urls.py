from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.blog_list, name='blog_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]