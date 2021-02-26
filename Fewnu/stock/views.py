



from django.http import HttpResponse
from django.shortcuts import render
from . models import Stock




# Create your views here.
def stock(request):
     
     return render(request, "stock/stock.html") 
                                                                  



   