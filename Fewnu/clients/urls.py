from django.urls import path
from . import views
app_name='client'

urlpatterns = [
    path('client/', views.clients, name='client'),
]