from django.contrib import admin
from .models import Actor

class ActorAdmin(admin.ModelAdmin):
	list_display = ('names', 'get_avatar')

admin.site.register(Actor, ActorAdmin)

