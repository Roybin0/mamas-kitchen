# Generated by Django 3.2.16 on 2023-01-29 20:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20230129_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='reply',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]