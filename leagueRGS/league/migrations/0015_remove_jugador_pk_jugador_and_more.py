# Generated by Django 4.1.7 on 2023-04-14 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0014_remove_jugador_pk_jugador_jugador_pk_jugador'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='jugador',
            name='pk_jugador',
        ),
        migrations.RemoveConstraint(
            model_name='partido',
            name='unique_match',
        ),
        migrations.RemoveConstraint(
            model_name='partido',
            name='unique_match',
        ),
    ]
