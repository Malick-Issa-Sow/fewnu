from django.urls import path
from . import views
app_name='boutique'

urlpatterns = [
    path('boutique/', views.boutique, name='boutique'),
]
