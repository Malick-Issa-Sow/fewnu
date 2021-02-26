from django.contrib import admin


from .models import Boutique

# Register your models here.
class BoutiqueAdmin(admin.ModelAdmin): #serve pour personnaliser l'administrateur
    list_display = ['nom_boutique', 'adresse','email_boutique','telephone_boutique','created_at', 'updated_at']
    search_fields = ['nom_boutique', 'adresse','telephone_boutique',] #fields disponibles pour la recherche

admin.site.register(Boutique, BoutiqueAdmin)
