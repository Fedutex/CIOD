from django.contrib import admin

from .models import Paciente, Odontologo, Blog

admin.site.register(Paciente)
admin.site.register(Odontologo)
admin.site.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'created_at')  # Campos a mostrar en la lista
    search_fields = ('title', 'autor')                # Campos que se pueden buscar