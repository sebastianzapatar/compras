# Generated by Django 3.0.5 on 2020-04-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0008_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
