# Generated by Django 4.1.7 on 2023-03-23 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_alter_evento_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='equipo',
            field=models.ForeignKey(default='JHJHJHJ', on_delete=django.db.models.deletion.CASCADE, to='league.equipo'),
        ),
    ]