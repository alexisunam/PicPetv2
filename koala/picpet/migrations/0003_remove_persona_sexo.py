# Generated by Django 4.0.4 on 2022-05-16 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picpet', '0002_alter_persona_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='sexo',
        ),
    ]
