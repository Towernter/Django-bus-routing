# Generated by Django 2.2.6 on 2019-10-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('driver_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=50)),
                ('estimated_people', models.IntegerField()),
                ('route_name', models.CharField(max_length=20)),
                ('time_line', models.IntegerField()),
            ],
        ),
    ]
