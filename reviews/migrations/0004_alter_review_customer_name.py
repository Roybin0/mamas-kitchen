# Generated by Django 3.2.16 on 2023-01-29 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230129_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='customer_name',
            field=models.CharField(max_length=100),
        ),
    ]