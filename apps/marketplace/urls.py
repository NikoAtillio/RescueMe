from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'marketplace'

urlpatterns = [
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('centres/', views.centre_list, name='centre_list'),
    path('centres/<int:pk>/', views.centre_detail, name='centre_detail'),
    path('search/', views.search_results, name='search_results'),
    path('search/autocomplete/', views.search_autocomplete, name='search_autocomplete'),
    path('animals/search-form/', views.animal_search_form, name='animal_search_form'),
    path('centres/search-form/', views.centre_search_form, name='centre_search_form'),
    path('animal-quick-view/<int:pk>/', views.animal_quick_view, name='animal_quick_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)