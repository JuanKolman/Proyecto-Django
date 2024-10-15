# admin.py
from django.contrib import admin
from .models import Cuestionario, Pregunta, Respuesta, Estado, Parroquia, Municipio, User, Report

# Register your models here.
admin.site.register(Cuestionario)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Estado)
admin.site.register(Parroquia)
admin.site.register(Municipio)
admin.site.register(User)
admin.site.register(Report)