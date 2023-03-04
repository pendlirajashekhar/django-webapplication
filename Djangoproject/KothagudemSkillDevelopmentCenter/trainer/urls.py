from django.urls import path
from . import views
urlpatterns = [
    path('',views.trainerlogin,name='trainerlogin'),
    path('trainerhome',views.trainerhome,name='trainerhome'),
    path('traineregistration',views.Trainerregistration,name='traineregistration'),
    path('trainerviewsall',views.trainerviewall,name='trainerviewall'),
    path('trainerprofile',views.trainerprofile,name='trainerprofile'),
    path('traineradddetails',views.traineradddetails,name='traineradddetails'),
    path ('trainercredits',views.trainercredits,name='trainercredits'),
    path ('deletet/<id>',views.deletetrainer,name='deletet'),
    
]