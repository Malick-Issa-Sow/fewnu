
from django.http import HttpResponse
from django.shortcuts import render
from . models import Pret

# Create your views here.
def pret(request):
   
    return render(request, "pret/pret.html") 
                                                                  



   