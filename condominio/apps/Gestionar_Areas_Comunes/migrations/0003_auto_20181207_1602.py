# Generated by Django 2.1.4 on 2018-12-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Areas_Comunes', '0002_auto_20181207_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar_horarios_para_reserva',
            name='área',
            field=models.ForeignKey(null=True, on_delete='do_nothing', to='Gestionar_Areas_Comunes.Area'),
        ),
    ]
