# Generated by Django 2.2.6 on 2019-10-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='door_public_key',
            field=models.CharField(default='DEFAULT', max_length=256),
        ),
    ]
