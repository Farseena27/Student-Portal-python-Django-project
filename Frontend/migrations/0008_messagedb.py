# Generated by Django 3.2.10 on 2023-09-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0007_applicationdb_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('Message', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
