# Generated by Django 2.2.6 on 2019-12-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20191205_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='input_auth',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
