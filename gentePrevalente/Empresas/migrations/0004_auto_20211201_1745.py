# Generated by Django 3.2.9 on 2021-12-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresas', '0003_estadoempresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='aprobacion',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.DeleteModel(
            name='EstadoEmpresa',
        ),
    ]
