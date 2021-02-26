from django.contrib import admin


from .models import Stock

# Register your models here.
class StockAdmin(admin.ModelAdmin): #serve pour personnaliser l'administrateur
    list_display = ['produits', 'prix_unitaire','quantite','created_at', 'updated_at']
    search_fields = ['produits', 'prix_unitaire','quantite','created_at', 'updated_at'] #fields disponibles pour la recherche
    prepopulated_fields = {'produits': ('produits',)}

admin.site.register(Stock, StockAdmin)
