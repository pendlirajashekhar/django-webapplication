from django.urls import path
from . import views
urlpatterns = [
    path('',views.StudentLogin,name='Studentlogin'),
    path('studenthome',views.Studenthome,name='Studenthome'),
    path('StudentRegistartion',views.Studentregistration,name='StudentRegistartion'),
    path('Studentview',views.Studentview,name='studentview'),
    path('studentprofile',views.studentprofile,name='studentprofile'),
    path('studentapplication',views.studentapplication,name='studentapplication'),
    
]
