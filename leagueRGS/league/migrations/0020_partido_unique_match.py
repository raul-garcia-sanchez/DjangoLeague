# Generated by Django 4.1.7 on 2023-04-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0019_remove_partido_unique_match'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='partido',
            constraint=models.UniqueConstraint(fields=('local', 'visitante'), name='unique_match'),
        ),
    ]