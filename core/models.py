### **Modelos de Django para `core/models.py`**


from django.db import models

# Tipo de Identificación
class TipoIdentificacion(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo


# Persona
class Persona(models.Model):
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    identificacion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Usuario
class Usuario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default='activo')

    def __str__(self):
        return self.username


# Supervisor
class Supervisor(models.Model):
    supervisor = models.ForeignKey(Usuario, related_name='supervisados', on_delete=models.CASCADE)
    subordinado = models.ForeignKey(Usuario, related_name='supervisores', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.supervisor} supervisa a {self.subordinado}"


# Perfil
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Rol
class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# Permiso de Página Web
class PermisoPagina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.nombre


# Privilegio de Acción en Página Web
class PrivilegioAccion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    nivel = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# Usuario-Perfil
class UsuarioPerfil(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'perfil')


# Perfil-Rol
class PerfilRol(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('perfil', 'rol')


# Rol-Permiso
class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(PermisoPagina, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rol', 'permiso')


# Rol-Privilegio
class RolPrivilegio(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    privilegio = models.ForeignKey(PrivilegioAccion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rol', 'privilegio')


# Módulo
class Modulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    permiso = models.ForeignKey(PermisoPagina, on_delete=models.CASCADE)
    categoria = models.ForeignKey('CategoriaModulo', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# Submódulo
class SubModulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey('CategoriaModulo', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# Usuario-Submódulo
class UsuarioSubModulo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    submodulo = models.ForeignKey(SubModulo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'submodulo')


# Permiso-Submódulo
class PermisoSubModulo(models.Model):
    permiso = models.ForeignKey(PermisoPagina, on_delete=models.CASCADE)
    submodulo = models.ForeignKey(SubModulo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('permiso', 'submodulo')


# Privilegio-Submódulo
class PrivilegioSubModulo(models.Model):
    privilegio = models.ForeignKey(PrivilegioAccion, on_delete=models.CASCADE)
    submodulo = models.ForeignKey(SubModulo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('privilegio', 'submodulo')


# Privilegio-Usuario
class PrivilegioUsuario(models.Model):
    privilegio = models.ForeignKey(PrivilegioAccion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('privilegio', 'usuario')


# Auditoría (singular) 
class Auditoria(models.Model): 
    tabla = models.CharField(max_length=100)  # Tabla afectada
    accion = models.CharField(max_length=100)  # Acción realizada
    registro_id = models.IntegerField()  # ID del registro afectado
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)  # Usuario que realiza la acción
    detalle = models.TextField(blank=True, null=True)  # Detalle del cambio
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la acción

    def __str__(self):
        return f"{self.tabla} - {self.accion} - {self.fecha}"


# Jerarquía de Roles
class JerarquiaRol(models.Model):
    rol = models.ForeignKey(Rol, related_name='rol_hijo', on_delete=models.CASCADE)
    rol_padre = models.ForeignKey(Rol, related_name='rol_padre', on_delete=models.CASCADE)


# Categoría de Módulo
class CategoriaModulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# Token de Sesión
class TokenSesion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    ip = models.GenericIPAddressField(blank=True, null=True)
    dispositivo = models.CharField(max_length=255, blank=True, null=True)
    inicio_sesion = models.DateTimeField(auto_now_add=True)
    fin_sesion = models.DateTimeField(blank=True, null=True)
    activa = models.BooleanField(default=True)


# Registro de Actividades
class RegistroActividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    accion = models.CharField(max_length=100)
    detalle = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)


# Log del Sistema
class LogSistema(models.Model):
    tipo = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


# Aprobaciones
class Aprobacion(models.Model):
    accion = models.CharField(max_length=100)
    detalle = models.TextField(blank=True, null=True)
    usuario_peticion = models.ForeignKey(Usuario, related_name='peticiones_aprobacion', on_delete=models.CASCADE)
    usuario_aprobacion = models.ForeignKey(Usuario, related_name='aprobaciones', on_delete=models.CASCADE, null=True, blank=True)
    estado = models.CharField(max_length=50, default='pendiente')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario_peticion.persona.nombre} {self.usuario_peticion.persona.apellido} - {self.accion} - {self.estado}"



# Transacciones Financieras
class TransaccionFinanciera(models.Model):
    tipo = models.CharField(max_length=100)  # Ingreso, Egreso
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey('CategoriaTransaccion', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto}"


# Categoría de Transacción
class CategoriaTransaccion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Activos
class Activo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_adquisicion = models.DateTimeField(blank=True, null=True)
    vida_util_estimada = models.IntegerField(blank=True, null=True)  # En meses
    estado = models.CharField(max_length=50, default='activo')

    def __str__(self):
        return self.nombre


# Mantenimientos
class Mantenimiento(models.Model):
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)  # Preventivo, Correctivo
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    proximo_mantenimiento = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.activo.nombre}"


# Parqueaderos
class Parqueadero(models.Model):
    numero = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default='disponible')  # Disponible, Ocupado, etc.
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.numero


# Citofonía
class Citofonia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    destinatario = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='pendiente')  # Pendiente, Finalizada

    def __str__(self):
        return f"{self.usuario.username} -> {self.destinatario}"


# Eventos de Videovigilancia
class EventoVideovigilancia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    rostro_detectado = models.TextField(blank=True, null=True)
    ubicacion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    accion_sugerida = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Evento en {self.ubicacion} - {self.fecha}"


# Auditorías (plural)
class Auditorias(models.Model):  # Nota: he usado el plural para que coincida con la tabla SQL
    tipo = models.CharField(max_length=100)  # Interna, Externa
    descripcion = models.TextField(blank=True, null=True)  # Descripción de la auditoría
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la auditoría
    resultado = models.TextField(blank=True, null=True)  # Resultado de la auditoría
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)  # Usuario que ejecuta la auditoría

    def __str__(self):
        return f"{self.tipo} - {self.fecha} - {self.usuario.username}"


# Reclutamiento
class Reclutamiento(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)  # Vigilante, Administrador, etc.
    estado = models.CharField(max_length=50, default='pendiente')  # Pendiente, Aprobado, Rechazado
    fecha_aplicacion = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"


# Reportes de Crímenes
class ReporteCrimen(models.Model):
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Crimen en {self.ubicacion} - {self.fecha}"


# Cuotas Extraordinarias
class CuotaExtraordinaria(models.Model):
    motivo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_recaudo = models.DateTimeField()
    justificacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.motivo} - {self.monto}"


# Tareas
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=50, default='pendiente')  # Pendiente # Pendiente, en_progreso, completada
    submodulo = models.ForeignKey(SubModulo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Tarea {self.nombre} - {self.estado}"


# Asignación de Tareas a Usuarios
class TareaUsuario(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tarea', 'usuario')


# Notificaciones
class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)  # Indica si la notificación fue leída

    def __str__(self):
        return f"Notificación para {self.usuario.username}"


# Proyectos
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# Relación entre Proyectos y Submódulos
class ProyectoSubModulo(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    submodulo = models.ForeignKey(SubModulo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('proyecto', 'submodulo')


# Registro de Cambios
class RegistroCambio(models.Model):
    tabla_afectada = models.CharField(max_length=100)  # Nombre de la tabla afectada
    columna_afectada = models.CharField(max_length=100, blank=True, null=True)  # Columna afectada (si aplica)
    registro_id = models.IntegerField()  # ID del registro modificado
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)  # Usuario que realizó el cambio
    accion = models.CharField(max_length=50)  # Acción realizada: insert, update, delete
    valor_anterior = models.TextField(blank=True, null=True)  # Valor antes del cambio
    valor_nuevo = models.TextField(blank=True, null=True)  # Valor después del cambio
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha del cambio

    def __str__(self):
        return f"{self.accion} en {self.tabla_afectada} por {self.usuario}"


# Sesiones
class Sesion(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)  # Usuario asociado a la sesión
    token = models.CharField(max_length=255)  # Token de la sesión
    ip = models.GenericIPAddressField(blank=True, null=True)  # Dirección IP del usuario
    dispositivo = models.CharField(max_length=255, blank=True, null=True)  # Dispositivo desde el cual inició la sesión
    inicio_sesion = models.DateTimeField(auto_now_add=True)  # Fecha de inicio de la sesión
    fin_sesion = models.DateTimeField(blank=True, null=True)  # Fecha de fin de la sesión
    activa = models.BooleanField(default=True)  # Si la sesión está activa o no

    def __str__(self):
        return f"Sesión de {self.usuario.username}"


# Personalización de Roles
class PersonalizacionRol(models.Model):
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)  # Rol asociado
    permiso = models.ForeignKey('PermisoPagina', on_delete=models.CASCADE)  # Permiso específico asociado
    limite_de_uso = models.IntegerField(blank=True, null=True)  # Número máximo de usos para este permiso

    def __str__(self):
        return f"Rol: {self.rol.nombre} - Permiso: {self.permiso.nombre}"
