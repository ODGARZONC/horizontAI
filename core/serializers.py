from rest_framework import serializers
from .models import Aprobacion

class AprobacionSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.SerializerMethodField()

    class Meta:
        model = Aprobacion
        fields = ['id', 'accion', 'detalle', 'usuario_peticion', 'usuario_aprobacion', 'estado', 'fecha', 'nombre_completo']

    def get_nombre_completo(self, obj):
        # Obteniendo el nombre completo del usuario peticionario desde Persona
        return f"{obj.usuario_peticion.persona.nombre} {obj.usuario_peticion.persona.apellido}"