# Generated by Django 3.2.8 on 2022-12-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mod_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalvariables',
            name='description',
            field=models.TextField(max_length=1050, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='globalvariables',
            name='value',
            field=models.TextField(max_length=1050, verbose_name='Value'),
        ),
    ]
