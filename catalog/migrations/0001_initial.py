# Generated by Django 2.2.6 on 2019-10-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netid', models.CharField(default='DEFAULT', help_text='What is your NetID?', max_length=100)),
                ('first_name', models.CharField(default='DEFAULT', max_length=100)),
                ('last_name', models.CharField(default='DEFAULT', max_length=100)),
                ('user_public_key', models.CharField(default='DEFAULT', max_length=256)),
                ('door_accessed', models.ManyToManyField(to='catalog.Door')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
