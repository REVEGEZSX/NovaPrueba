# Generated by Django 2.1 on 2019-09-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20190910_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='Estado',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
