# Generated by Django 3.2.16 on 2023-01-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(max_length=100)),
                ('customer_phone', models.IntegerField()),
                ('party_size', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('sp_occasion', models.BooleanField(default=False)),
                ('sp_requirements', models.BooleanField(default=False)),
                ('confirmed', models.IntegerField(default=0, verbose_name=((0, 'Not confirmed'), (1, 'Confirmed')))),
            ],
        ),
    ]
