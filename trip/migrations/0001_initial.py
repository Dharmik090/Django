# Generated by Django 4.2.11 on 2024-05-07 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripPlan',
            fields=[
                ('trip_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('departure_place', models.CharField(max_length=30)),
                ('return_date', models.DateField()),
                ('return_time', models.TimeField()),
                ('return_place', models.CharField(max_length=30)),
                ('duration', models.IntegerField(default=0)),
                ('extra_info', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='trip_thumbnail/')),
                ('agency_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.agency')),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('att_name', models.CharField(max_length=30, unique=True)),
                ('att_imgs', models.ImageField(upload_to='attraction/')),
                ('trip_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.tripplan')),
            ],
        ),
    ]