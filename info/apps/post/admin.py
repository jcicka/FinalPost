from django.contrib import admin
from .models import Post, Comentario

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'contenido', 'fecha_creacion')
	list_filter = ('titulo','fecha_creacion')

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('contenido', 'fecha_hora')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
