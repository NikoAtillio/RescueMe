from django.urls import path
from . import views

app_name = 'rescue'
urlpatterns = [
    path('animals/', views.animal_list, name='animal_list'),
    path('centers/', views.center_list, name='center_list'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('center/<int:pk>/', views.center_detail, name='center_detail'),
]