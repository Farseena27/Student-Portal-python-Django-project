from django.contrib import admin

# Register your models here.
from Backend.models import Coursedb,Jobdb

admin.site.register(Coursedb)
admin.site.register(Jobdb)