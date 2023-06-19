# Generated by Django 4.2.2 on 2023-06-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('body_type', models.CharField(max_length=100)),
                ('engine_volume', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='CarModel',
        ),
    ]