# Generated by Django 3.0.4 on 2020-03-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipapp', '0002_remove_recipe_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
    ]
