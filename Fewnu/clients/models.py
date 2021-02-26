from django.db import models

class Client(models.Model):
	nom = models.CharField('Nom', max_length=100)
	adresse = models.TextField('l\'adresse du client', blank=True)
	id_client = models.IntegerField('l\'identifiant du client', blank=True, default=0) #juste d\'organiser sur le backend
	telephone_client = models.IntegerField('telephone_client', blank=True, default=0) #juste d\'organiser sur le backend
	#connecting classes avec le cours
	created_at = models.DateTimeField('Créé de compte cliet',
									  auto_now_add=True)  # auto maintenant à chaque fois q créer un cours, il définit automatiquement la date
	updated_at = models.DateTimeField('Mis à jour  du compte du client',
									  auto_now_add=True)  # dès qu'il est rafraîchi la date entre seule

	def __str__(self):
		return self.nom