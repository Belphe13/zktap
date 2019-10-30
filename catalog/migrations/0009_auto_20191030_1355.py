# Generated by Django 2.2.6 on 2019-10-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_user_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='door',
            field=models.ManyToManyField(choices=[('N/A', 'N/A'), ('P', 'Pending'), ('D', 'Denied'), ('A', 'Approved')], to='catalog.Door'),
        ),
    ]
