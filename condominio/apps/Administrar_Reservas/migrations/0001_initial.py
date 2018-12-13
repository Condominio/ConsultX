# Generated by Django 2.1.4 on 2018-12-13 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrar_Visitas', '0003_visita'),
        ('Gestionar_Areas_Comunes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_Reserva', models.DateTimeField(auto_now=True, null=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrar_Visitas.Propietario')),
                ('Áreas_Disponibles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestionar_Areas_Comunes.Asignar_Horarios_para_Reserva')),
            ],
        ),
    ]
