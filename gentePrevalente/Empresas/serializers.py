from rest_framework import serializers
from .models import Empresa,ArchivosEmpresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ["id","identificacion", "nombre", "razon_social", "NIT", "num_empleados","logo","aprobacion"]


class RelacionEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ["id","identificacion", "nombre", "razon_social", "NIT", "num_empleados","logo","aprobacion"]
        depth = 1

class ArchivosEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivosEmpresa
        fields = ["id","ruta_archivo", "empresa"]

class RelacionArchivosEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivosEmpresa
        fields = ["id","ruta_archivo", "empresa"]
        depth = 1