from django.urls import path
from . import views

urlpatterns=[
    path('',views.Adminlogin,name='Adminlogin'),
    path('adminhome',views.Adminhome,name='adminhome'),
    path('adminviewall',views.Adminviewall,name='adminviewall'),
    path('admineventadd',views.AdminEventadd,name='admineventadd'),
    path('adminprofile',views. Adminprofile,name='adminprofile'),
    path('adminapprover',views.Adminapprover,name='adminapprover'),
    
]