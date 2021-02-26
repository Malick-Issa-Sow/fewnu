from django.contrib import admin


from .models import Vente

# Register your models here.
class VenteAdmin(admin.ModelAdmin): #serve pour personnaliser l'administrateur
    list_display = ['nom_client', 'designation','quantite','prix', 'remise','prix_unitaire_achat',]
    search_fields = ['nom_client', 'designation','quantite','prix', 'remise','prix_unitaire_achat',] #fields disponibles pour la recherche
    prepopulated_fields = {'nom_client': ('nom_client',)}

admin.site.register(Vente, VenteAdmin)
