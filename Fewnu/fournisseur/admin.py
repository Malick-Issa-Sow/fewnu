from django.contrib import admin


from .models import Fournisseur

# Register your models here.
class FournisseurAdmin(admin.ModelAdmin): #serve pour personnaliser l'administrateur
    list_display = ['nom_fournisseur', 'adresse','email_fournisseur','telephone_fournisseur','created_at', 'updated_at']
    search_fields = ['nom_fournisseur', 'adresse','telephone_fournisseur',] #fields disponibles pour la recherche

admin.site.register(Fournisseur, FournisseurAdmin)
