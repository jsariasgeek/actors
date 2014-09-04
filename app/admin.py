from django.contrib import admin
from .models import Country, Actor


class CountryAdmin(admin.ModelAdmin):
	pass


class ActorAdmin(admin.ModelAdmin):

	list_display = ('names', 'get_avatar')

admin.site.register(Country,CountryAdmin)
admin.site.register(Actor, ActorAdmin)

