from django.urls import path
from . import views

urlpatterns=[
    path('',views.Companylogin,name='Companylogin'),
    path('companyregistration',views.Companyregistration,name='companyregistration'),
    path('Companyhome',views.Companyhome,name='CompanyHome'),
    path('Companyapplicants',views.Companyapplicants,name='Companyapplicants'),
    path('Companynotification',views.Companynotification,name='companynotification'),
    path('companyjobpost',views.companyjobpost,name='companyjobpost'),
    path('companyprofile',views.companyprofile,name='companyprofile'),
   
]