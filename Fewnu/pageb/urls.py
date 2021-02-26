from django.urls import path
from . import views
app_name='pageb'

urlpatterns = [
    path('', views.base, name='base'),
]