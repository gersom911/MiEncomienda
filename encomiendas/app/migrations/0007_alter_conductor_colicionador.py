# Generated by Django 4.1.3 on 2022-11-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_encomienda_evaluacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='colicionador',
            field=models.IntegerField(blank=True, null=True, verbose_name='colicionador'),
        ),
    ]