# Generated by Django 3.2.10 on 2023-09-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_jobdb_industry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCetogory',
            fields=[
                ('coursecat_id', models.AutoField(primary_key=True, serialize=False)),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
