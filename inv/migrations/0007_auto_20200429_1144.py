# Generated by Django 3.0.5 on 2020-04-29 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0006_producto'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together={('codigo', 'codigo_barra')},
        ),
    ]