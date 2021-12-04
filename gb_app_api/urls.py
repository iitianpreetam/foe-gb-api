from django.urls import path
from .views import get_gb, get_gb_level

urlpatterns = [
    path('get_gb/', get_gb, name='get_gb'),
    path('get_gb_level/', get_gb_level, name='get_gb_level')  
]
