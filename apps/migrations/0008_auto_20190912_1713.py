# Generated by Django 2.1 on 2019-09-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_auto_20190912_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='Foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/', verbose_name='Cargar imagen'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/', verbose_name='Cargar imagen'),
        ),
    ]
