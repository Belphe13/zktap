# Generated by Django 2.2.6 on 2019-10-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20191030_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='door_public_key',
            field=models.CharField(max_length=256),
        ),
        migrations.RemoveField(
            model_name='user',
            name='door_accessed',
        ),
        migrations.AddField(
            model_name='user',
            name='door_accessed',
            field=models.ManyToManyField(blank=True, to='catalog.Door'),
        ),
    ]
