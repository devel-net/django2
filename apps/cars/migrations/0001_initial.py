# Generated by Django 4.2.2 on 2023-06-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('body_type', models.CharField(max_length=25)),
                ('engine_volume', models.FloatField()),
            ],
        ),
    ]