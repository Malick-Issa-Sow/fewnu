
from django.http import HttpResponse
from django.shortcuts import render
from . models import Vente




# Create your views here.
def vente(request):
    return render(request,  "vente/vente.html")
