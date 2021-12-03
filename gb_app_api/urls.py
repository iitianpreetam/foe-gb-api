from django.urls import path
from .views import get_gb

urlpatterns = [
    path('get_gb/', get_gb, name='get_gb')    
]
