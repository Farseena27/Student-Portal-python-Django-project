# Generated by Django 3.2.10 on 2023-08-30 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_jobdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdb',
            old_name='salary',
            new_name='Salary',
        ),
    ]
