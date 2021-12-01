# Generated by Django 3.2.9 on 2021-11-30 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Empresas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='identificacion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.CharField(max_length=4096),
        ),
        migrations.CreateModel(
            name='ArchivosEmpresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruta_archivo', models.CharField(max_length=512)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresas.empresa')),
            ],
        ),
    ]