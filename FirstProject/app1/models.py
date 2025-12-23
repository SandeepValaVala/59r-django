from django.db import models

# Create your models here.

class Students(models.Model):
    Stud_name = models.CharField(max_length=100)
    Stud_age = models.IntegerField()
    Stud_gender = models.CharField(max_length=100)
    Stud_email = models.EmailField(unique=True)
 
 
class Employees(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_age = models.IntegerField()
    emp_gender = models.CharField(max_length=100)
    emp_email = models.EmailField(unique=True)   