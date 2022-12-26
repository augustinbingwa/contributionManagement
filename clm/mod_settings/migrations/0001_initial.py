# Generated by Django 3.2.8 on 2022-12-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalVariables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=50, verbose_name='Group')),
                ('key', models.CharField(max_length=50, verbose_name='Key')),
                ('value', models.TextField(max_length=1024, verbose_name='Value')),
                ('description', models.TextField(max_length=1024, verbose_name='Description')),
            ],
            options={
                'ordering': ('group', 'key'),
                'unique_together': {('group', 'key')},
                'index_together': {('group', 'key')},
            },
        ),
    ]
