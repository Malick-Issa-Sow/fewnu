
from django.http import HttpResponse
from django.shortcuts import render
from . models import Client


# Create your views here.
def clients(request):
    
    return render(request, "clients/clients.html") 
                                                                  



   