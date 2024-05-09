from rest_framework import serializers
from .models import Company,Employee

# ComapanySerializer class is made to do serialization and deserialization instances of the company class
class CompanySerializer(serializers.ModelSerializer):
    
    # ModelSerializer is provided by Django rest framework contains default create or update implementation
    class Meta:
        company_id= serializers.ReadOnlyField()
        # inner class of django serializer used to provide metadata  for the serializer
        model = Company
        fields = '__all__'  # This includes all fields of the Company model
 
class EmployeeSerializer(serializers.ModelSerializer):
    Emp_id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields='__all__'