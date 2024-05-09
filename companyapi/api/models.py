from django.db import models

# Create your models here.

#Creating class Company inherits models.Model which is the base class for all Django classes 
class Company (models.Model): 
    #defining fields of the company class
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=20,choices=(('IT','IT'),
                                                 ('Non-IT','Non-IT'),
                                                 ('Mobile','Mobile')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


class Employee(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    position=models.CharField(max_length=50,choices=
                              (('Manager','MNG'),
                               ('Software','SWE'),
                               ('Team Lead','TL')))
    company=models.ForeignKey(Company, default=1, on_delete=models.CASCADE)