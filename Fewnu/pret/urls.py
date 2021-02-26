from django.urls import path
from . import views
app_name='pret'

urlpatterns = [
    path('pret/', views.pret,name="pret"),
]
