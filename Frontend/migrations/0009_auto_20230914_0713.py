# Generated by Django 3.2.10 on 2023-09-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0008_messagedb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationdb',
            name='id',
        ),
        migrations.AddField(
            model_name='applicationdb',
            name='Aplctn_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
