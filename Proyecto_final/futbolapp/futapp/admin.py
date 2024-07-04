from django.contrib import admin
from .models import Equipo, Profesor, Jugador, Pago

admin.site.register(Equipo)
admin.site.register(Profesor)
admin.site.register(Jugador)
admin.site.register(Pago)