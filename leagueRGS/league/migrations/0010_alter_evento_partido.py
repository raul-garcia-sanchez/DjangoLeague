# Generated by Django 4.1.7 on 2023-03-24 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0009_alter_evento_partido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='partido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.partido'),
        ),
    ]
