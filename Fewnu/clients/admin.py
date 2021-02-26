from django.contrib import admin


from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin): #serve pour personnaliser l'administrateur
    list_display = ['nom', 'adresse','telephone_client','created_at', 'updated_at']
    search_fields = ['nom', 'adresse','telephone_client',] #fields disponibles pour la recherche
    prepopulated_fields = {'nom': ('nom',)}

admin.site.register(Client, ClientAdmin)
