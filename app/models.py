from django.db import models

class Actor(models.Model):

	genres = (('M','Masculino'), ('F','Femenino'))

	names = models.CharField(max_length=60)
	picture = models.ImageField()
	genre = models.CharField(max_length=1, choices=genres)
