from django.db import models

class Boutique(models.Model):
	nom_boutique = models.CharField('Nom boutique', max_length=100)
	id_mesboutique= models.IntegerField('l\'identifiant de mes boutiques', blank=True, default=0) #juste d\'organiser sur le backend
	adresse = models.TextField('l\'adresse de la boutiques', blank=True)
	id_boutique= models.IntegerField('l\'identifiant de la boutique', blank=True, default=0) #juste d\'organiser sur le backend
	telephone_boutique = models.IntegerField('telephone_boutique', blank=True, default=0) #juste d\'organiser sur le backend
	email_boutique = models.EmailField('email boutique',max_length=254)
	mots_passe = models.CharField('le mots de passe de la boutique',max_length=254),
	confirme_mots_passe = models.CharField('confirme le mots de passe de la boutique',max_length=254)
	#connecting classes avec le cours
	created_at = models.DateTimeField('Créé de compte cliet',
									  auto_now_add=True)  # auto maintenant à chaque fois q créer un cours, il définit automatiquement la date
	updated_at = models.DateTimeField('Mis à jour  du compte du boutique',
									  auto_now_add=True)  # dès qu'il est rafraîchi la date entre seule

	def __str__(self):
		return self.nom_boutique