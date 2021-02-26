from django.db import models

class Vente(models.Model):
	nom_client = models.CharField('Nom vente', max_length=100)
	id_boutique= models.IntegerField('l\'identifiant de boutique', blank=True, default=0)
	id_vente= models.IntegerField('l\'identifiant de mes ventes', blank=True, default=0) #juste d\'organiser sur le backend
	designation= models.CharField('designation', max_length=100, blank=True, default=0) 
	quantite= models.IntegerField('quantite', blank=True, default=0) #juste d\'organiser sur le backend
	prix= models.IntegerField('prix', blank=True, default=0)
	remise= models.IntegerField('remise', blank=True, default=0) #juste d\'organiser sur le backend
	prix_unitaire_achat= models.IntegerField('prix unitaire d\'achat, blank=True, default=0') #juste d\'organiser sur le backend
	prix_unitaire_vente= models.IntegerField('prix unitaire de vente, blank=True, default=0') #juste d\'organiser sur le backend
	#juste d\'organiser sur le backend
	#connecting classes avec le cours
	created_at = models.DateTimeField('Créé de compte cliet',
									  auto_now_add=True)  # auto maintenant à chaque fois q créer un cours, il définit automatiquement la date
	updated_at = models.DateTimeField('Mis à jour  du compte du vente',
									  auto_now_add=True)  # dès qu'il est rafraîchi la date entre seule

	def __str__(self):
		return self.nom_client