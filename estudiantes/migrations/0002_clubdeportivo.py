# Generated by Django 3.0.5 on 2020-05-14 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubDeportivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, unique=True)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Estudiante')),
            ],
            options={
                'verbose_name_plural': 'Clubes',
            },
        ),
    ]
