from django.db import models

class Pret(models.Model):
	nom_client = models.CharField('Nom client', max_length=100)
	id_client= models.IntegerField('l\'identifiant du client', blank=True, default=0) #juste d\'organiser sur le backend
	id_pret= models.IntegerField('l\'identifiant de mes prets', blank=True, default=0) #juste d\'organiser sur le backend
	article = models.TextField('l\'article du prets', blank=True)
	montant = models.IntegerField('montant du pret', blank=True, default=0) #juste d\'organiser sur le backend
	#connecting classes avec le cours
	created_at = models.DateTimeField('Créé de compte cliet',
									  auto_now_add=True)  # auto maintenant à chaque fois q créer un cours, il définit automatiquement la date
	updated_at = models.DateTimeField('Mis à jour  du compte du pret',
									  auto_now_add=True)  # dès qu'il est rafraîchi la date entre seule

	def __str__(self):
		return self.nom_client 