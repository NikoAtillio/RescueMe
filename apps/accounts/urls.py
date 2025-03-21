from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('delete/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_view, name='logout'),
]