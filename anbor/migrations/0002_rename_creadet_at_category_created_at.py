# Generated by Django 5.0.1 on 2024-01-31 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anbor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='creadet_at',
            new_name='created_at',
        ),
    ]