# Generated by Django 4.2.4 on 2023-09-18 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
