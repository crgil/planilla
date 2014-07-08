from django.contrib import admin

# Register your models here.
from principal.models import empresa
from principal.models import cargo
from principal.models import unidad_medida
from principal.models import tarea
from principal.models import sector
from principal.models import lote
from principal.models import planilla
from principal.models import contratista
from principal.models import empleado_fijo
from principal.models import empleado_temp
from principal.models import diario_planilla
from principal.models import tipo_pago
from principal.models import pago

#para mostrar el detalle como un listado con los campos que quiero y no solo un campo
class DiarioPlanillaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'empleado_temp', 'tarea', 'lote','empleado_fijo']
    list_filter = ['fecha']
    search_fields = ['empleado_temp']

admin.site.register(empresa)
admin.site.register(cargo)
admin.site.register(unidad_medida)
admin.site.register(tarea)
admin.site.register(sector)
admin.site.register(lote)
admin.site.register(planilla)
admin.site.register(contratista)
admin.site.register(empleado_fijo)
admin.site.register(empleado_temp)
admin.site.register(diario_planilla, DiarioPlanillaAdmin)
admin.site.register(tipo_pago)
admin.site.register(pago)
