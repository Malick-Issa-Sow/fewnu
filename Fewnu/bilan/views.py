
from django.http import HttpResponse
from django.shortcuts import render




# Create your views here.
def bilan(request):
     return render(request, "bilan/bilan.html") 




   