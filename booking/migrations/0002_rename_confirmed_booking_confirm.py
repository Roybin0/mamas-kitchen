# Generated by Django 3.2.16 on 2023-01-29 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='confirmed',
            new_name='confirm',
        ),
    ]