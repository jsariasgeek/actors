from django.db import models

class Actor(models.Model):

	genres = (('M','Masculino'), ('F','Femenino'))

	names = models.CharField(max_length=60)
	picture = models.ImageField(upload_to='pictures')
	genre = models.CharField(max_length=1, choices=genres)

	def __unicode__(self):
		return self.names