from django.urls import path
from . import views
app_name='bilan'

urlpatterns = [
    path('bilan/', views.bilan, name='bilan'),
]