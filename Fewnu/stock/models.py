from django.db import models

class Stock(models.Model):
	id_boutique= models.IntegerField('l\'identifiant de boutique', blank=True, default=0)
	id_stock= models.IntegerField('l\'identifiant de mes stocks', blank=True, default=0) #juste d\'organiser sur le backend
	produits= models.CharField('produits', max_length=100, blank=True, default=0) 
	quantite= models.IntegerField('quantite', blank=True, default=0) #juste d\'organiser sur le backend
	prix_unitaire= models.IntegerField('prix unitaire ', blank=True, default=0) #juste d\'organiser sur le backend
	#juste d\'organiser sur le backend
	#connecting classes avec le cours
	created_at = models.DateTimeField('Créé de compte cliet',
									  auto_now_add=True)  # auto maintenant à chaque fois q créer un cours, il définit automatiquement la date
	updated_at = models.DateTimeField('Mis à jour  du compte du stock',
									  auto_now_add=True)  # dès qu'il est rafraîchi la date entre seule

	def __str__(self):
		return self.produits