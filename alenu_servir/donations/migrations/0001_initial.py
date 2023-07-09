# Generated by Django 4.2.1 on 2023-07-09 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificacion', models.CharField(max_length=20)),
                ('tipo_donante', models.CharField(max_length=20)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proposito', models.CharField(max_length=100)),
                ('fuente', models.CharField(max_length=100)),
                ('confirmado', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
