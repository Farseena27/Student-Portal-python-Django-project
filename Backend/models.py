from django.db import models


# Create your models here.
class Coursedb(models.Model):
    Course_id = models.AutoField(primary_key=True)
    Course = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Category= models.CharField(max_length=100, null=True, blank=True)
    Institution = models.CharField(max_length=100, null=True, blank=True)
    Contact=models.IntegerField(null=True,blank=True)
    Duration = models.CharField(max_length=100, null=True, blank=True)
    Fees = models.IntegerField(null=True, blank=True)

class CourseCetogorydb(models.Model):
    coursecat_id=models.AutoField(primary_key=True)
    Category= models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)


class Jobdb(models.Model):
    Job_id=models.AutoField(primary_key=True)
    Job_Name=models.CharField(max_length=100,null=True,blank=True)
    Industry=models.CharField(max_length=100,null=True,blank=True)
    Company=models.CharField(max_length=100,null=True,blank=True)
    Openings=models.IntegerField(null=True,blank=True)
    Experiance=models.CharField(max_length=100,null=True,blank=True)
    Location=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    Salary=models.IntegerField(null=True,blank=True)
    Employment_status=models.CharField(max_length=100,null=True,blank=True)

class JobCategorydb(models.Model):
    category_id=models.AutoField(primary_key=True)
    Industry=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)

