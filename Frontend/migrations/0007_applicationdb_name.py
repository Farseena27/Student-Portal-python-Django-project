# Generated by Django 3.2.10 on 2023-09-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0006_alter_signupdb_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdb',
            name='Name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
