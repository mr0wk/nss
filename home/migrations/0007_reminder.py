# Generated by Django 4.1 on 2022-08-22 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_city_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.connection')),
            ],
        ),
    ]
