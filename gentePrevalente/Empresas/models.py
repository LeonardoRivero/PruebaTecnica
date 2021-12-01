from django.db import models

# Create your models here.

class Empresa(models.Model):
    id=models.AutoField(primary_key=True)
    identificacion = models.IntegerField()
    nombre = models.CharField(max_length=120)
    razon_social = models.CharField(max_length=120)
    NIT = models.CharField(max_length=10)
    num_empleados= models.IntegerField()
    logo=models.CharField(max_length=4096)

    objects = models.Manager()

    def __str__(self):
        return 'Identificacion:%s Nombre:%s Razon Social:%s' % (self.identificacion, self.nombre, self.razon_social)

class ArchivosEmpresa(models.Model):
    id=models.AutoField(primary_key=True)
    ruta_archivo=models.CharField(max_length=512)
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)
