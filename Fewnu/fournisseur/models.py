from django.db import models

class Fournisseur(models.Model):
	nom_fournisseur = models.CharField('Nom fournisseur', max_length=100)
	id_fournisseur= models.IntegerField('l\'identifiant de mes fournisseurs', blank=True, default=0) #juste d\'organiser sur le backend
	adresse = models.TextField('l\'adresse de la fournisseurs', blank=True)
	telephone_fournisseur = models.IntegerField('telephone_fournisseur', blank=True, default=0) #juste d\'organiser sur le backend
	email_fournisseur = models.EmailField('email fournisseur',max_length=254)
	#connecting classes avec le cours
	created_at = models.DateTimeField('Créé de compte cliet',
									  auto_now_add=True)  # auto maintenant à chaque fois q créer un cours, il définit automatiquement la date
	updated_at = models.DateTimeField('Mis à jour  du compte du fournisseur',
									  auto_now_add=True)  # dès qu'il est rafraîchi la date entre seule

	def __str__(self):
		return self.nom_fournisseur