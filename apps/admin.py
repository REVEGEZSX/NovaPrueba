from django.contrib import admin

from .models import *

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Tipo_Profesional)
#admin.site.register(Profesional)
#admin.site.register(Paciente)
admin.site.register(Administrador)
admin.site.register(Registrar_Cita)
admin.site.register(Consulta)
admin.site.register(Detalle_Enfermedad)
admin.site.register(Enfermedad)
admin.site.register(Genero)

class ProfesionalAdmin(admin.ModelAdmin):
    model = Profesional
    list_display = ['Nombre','Apellido','Identificacion','Mostrar_foto']
    

    
    readonly_fields = ['Mostrar_foto']


admin.site.register(Profesional, ProfesionalAdmin)


class PacienteAdmin(admin.ModelAdmin):
    model = Paciente
    list_display = ['Nombre','Apellido','Identificacion','Mostrar_foto']
    

    
    readonly_fields = ['Mostrar_foto']

admin.site.register(Paciente, PacienteAdmin)


