# Generated by Django 4.2.5 on 2023-09-29 18:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='park_images')),
                ('date', models.DateField(default=datetime.date.today)),
                ('description', models.CharField(max_length=100)),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dogparks')),
            ],
        ),
    ]