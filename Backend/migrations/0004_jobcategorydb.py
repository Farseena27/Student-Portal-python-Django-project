# Generated by Django 3.2.10 on 2023-09-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_rename_salary_jobdb_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategorydb',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
