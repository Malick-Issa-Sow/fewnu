from django.contrib import admin


from .models import Pret

# Register your models here.
class PretAdmin(admin.ModelAdmin): #serve pour personnaliser l'administrateur
    list_display = ['nom_client', 'article','montant','created_at', 'updated_at']
    search_fields = ['nom client', 'article','montant',] #fields disponibles pour la recherche
    prepopulated_fields = {'nom_client': ('nom_client',)}

admin.site.register(Pret, PretAdmin)
