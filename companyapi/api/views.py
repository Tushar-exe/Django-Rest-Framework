from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
# Create your views here.

# CompanyViewSet inherits ModelViewSet which contains default actions like "C R U D"
class CompanyViewSet(viewsets.ModelViewSet): # This class is extending ModelViewSet which is present in viewsets

    #queryset contains all the objects 
    queryset= Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


