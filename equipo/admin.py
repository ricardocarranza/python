from django.contrib import admin
from models import Estado, Equipo, TipoEquipo, Unidad

# Register your models here.

"""class TipoEquipoAdmin:
	list_display = ('tipo_de_equipo',)"""

admin.site.register(TipoEquipo)
admin.site.register(Estado)
admin.site.register(Equipo)
admin.site.register(Unidad)