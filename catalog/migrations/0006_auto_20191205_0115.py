# Generated by Django 2.2.6 on 2019-12-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_externalinput'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_auth', models.CharField(default='0', max_length=100)),
                ('input_door_public_key', models.CharField(default='0', max_length=256)),
                ('input_userr_public_key', models.CharField(default='0', max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='ExternalInput',
        ),
    ]
