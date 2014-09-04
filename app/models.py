from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import datetime

class Country(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

	class Meta():
		ordering = ['name']


class Actor(models.Model):

	genres = (('M','Masculino'), ('F','Femenino'))

	names = models.CharField(max_length=60)
	picture = models.ImageField(upload_to='pictures')
	genre = models.CharField(max_length=1, choices=genres)
	birthday = models.DateField(default=datetime.date.today())
	country = models.ForeignKey(Country)
	avatar = ImageSpecField(source='picture', 
				processors=[ResizeToFill(100, 100)], 
				format='JPEG',
				options={'quality': 100}
				)

	def __unicode__(self):
		return self.names

	def get_avatar(self):
		return """<img src='%s' alt='%s'> """ %(self.avatar.url, self.names)

	get_avatar.short_description = 'Picture'
	get_avatar.allow_tags = True