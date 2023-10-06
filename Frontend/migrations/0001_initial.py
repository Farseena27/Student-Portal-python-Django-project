# Generated by Django 3.2.10 on 2023-09-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicationdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Job_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Industry', models.CharField(blank=True, max_length=100, null=True)),
                ('Company', models.CharField(blank=True, max_length=100, null=True)),
                ('Openings', models.IntegerField(blank=True, null=True)),
                ('Experiance', models.CharField(blank=True, max_length=100, null=True)),
                ('Location', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Salary', models.IntegerField(blank=True, null=True)),
                ('Employment_status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signupdb',
            fields=[
                ('Signup_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Password', models.CharField(blank=True, max_length=200, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Profile')),
                ('Location', models.CharField(blank=True, max_length=200, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('Jobpreference', models.CharField(blank=True, max_length=200, null=True)),
                ('Jobapplies', models.CharField(blank=True, max_length=200, null=True)),
                ('Resume', models.ImageField(blank=True, null=True, upload_to='Resume')),
            ],
        ),
    ]