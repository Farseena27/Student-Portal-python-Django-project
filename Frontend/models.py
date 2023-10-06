from django.db import models

# Create your models here.
class Signupdb(models.Model):
    Signup_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Password = models.CharField(max_length=200, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Image = models.ImageField(upload_to='Profile', null=True, blank=True)
    Location = models.CharField(max_length=200, null=True, blank=True)
    Qualification = models.CharField(max_length=200, null=True, blank=True)
    Jobpreference = models.CharField(max_length=200, null=True, blank=True)
    Jobapplies = models.CharField(max_length=200, null=True, blank=True)
    Resume = models.FileField(upload_to='Resume', null=True, blank=True)

class Applicationdb(models.Model):
    Aplctn_id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Japp_id=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Job_Name=models.CharField(max_length=100,null=True,blank=True)
    Industry = models.CharField(max_length=100, null=True, blank=True)
    Company = models.CharField(max_length=100, null=True, blank=True)
    Openings = models.IntegerField(null=True, blank=True)
    Experiance = models.CharField(max_length=100, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Salary = models.IntegerField(null=True, blank=True)
    Employment_status = models.CharField(max_length=100, null=True, blank=True)

class Messagedb(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email=models.EmailField(null=True,blank=True)
    subject=models.CharField(max_length=200, null=True, blank=True)
    Message=models.CharField(max_length=200, null=True, blank=True)



