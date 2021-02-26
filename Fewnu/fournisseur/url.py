from django.urls import path
from . import views
app_name='fournisseur'

urlpatterns = [
    path('', views.fournisseur, name='fournisseur'),
]

