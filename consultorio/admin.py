from django.contrib import admin

from .models import Paciente, Odontologo

admin.site.register(Paciente)
admin.site.register(Odontologo)