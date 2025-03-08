from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TipoIdentificacion)
admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Supervisor)
admin.site.register(Perfil)
admin.site.register(Rol)
admin.site.register(PermisoPagina)
admin.site.register(PrivilegioAccion)
admin.site.register(Auditoria)
admin.site.register(Sesion)
admin.site.register(PersonalizacionRol)
admin.site.register(Auditorias)
admin.site.register(Aprobacion)
# Registra más modelos según sea necesario...
