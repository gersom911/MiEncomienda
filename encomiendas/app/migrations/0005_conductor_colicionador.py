# Generated by Django 4.1.3 on 2022-11-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_evaluacion_conductor_alter_conductor_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='colicionador',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='colicionador'),
        ),
    ]