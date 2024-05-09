from django.contrib import admin

#we need to import our class from the same or current directory i.e (.models)
from .models import Company,Employee

# Register your models here.
@admin.register(Company)



#company class inherits from the ModelAdmin class provided by django Admin
class Company(admin.ModelAdmin):
    #specifying the list of columns which will be display in the admin page 
    list_display =['company_id','name','location','about','type','added_date','active']


@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display=['id','name','location']