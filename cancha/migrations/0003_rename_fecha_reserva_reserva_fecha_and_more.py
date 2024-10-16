# Generated by Django 5.1.2 on 2024-10-10 14:41

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancha', '0002_remove_stock_cantidad_bebida_cantidad_stock_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='fecha_reserva',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='horario',
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_fin',
            field=models.TimeField(default=datetime.time(10, 0)),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_inicio',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
