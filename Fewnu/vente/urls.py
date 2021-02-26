from django.urls import path
from . import views
app_name='vente'

urlpatterns = [
    path('vente/', views.vente,name='vente'),
]