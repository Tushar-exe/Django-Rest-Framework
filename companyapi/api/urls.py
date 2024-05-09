from django.contrib import admin
from django.urls import path,include
# from api.views taake companyViewSet 
from api.views import CompanyViewSet,EmployeeViewSet
# import router from rest_framework
from rest_framework import routers
#we want default router for that we have imported router from rest_framework

router = routers.DefaultRouter()
# now we need to register our router ---> register methods take 2 args(prefix,ViewSet)(f'companies'---> means our url will have companies )
router.register(f'companies',CompanyViewSet)
router.register(f'employees',EmployeeViewSet)

urlpatterns = [ 
    path('',include(router.urls)) # include method has router which will search the url on its own.
   
]