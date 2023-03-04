from django.http import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate,login
from . models import StudentRegistration
from Company . models import Companyjobpost
from trainer . models import TrainerAddDetails

# Create your views here.
def StudentLogin(request):
    if request.method=='POST':
        name=request.POST['slid']
        pad=request.POST['spd']
        newuser=authenticate(username=email,password=password)
        if newuser is not None:
            login(request,newuser)
        return HttpresopnseRedirect('/Studenthome/')
        return render(request,'StudentHome.html')
    else:
        return render(request,'StudentLogin.html')
def Studenthome(request):
    return render(request,'StudentHome.html')
def Studentregistration(request):
    if request.method=='POST':
       Name=request.POST['sname']
       ema= request.POST['semial']
       num=request.POST['sn']
       add=request.POST['sad']
       pas=request.POST['spd']
       gender=request.POST['gender']
       van=StudentRegistration(name=Name,email=ema,number=num,adderss=add,password=pas,Gender=gender)
       van.save()
       newuser=authenticate(username=ema,password=pas)
       if newuser is not None:
        login(request,newuser)
        return HttpResopnseRedirect('/Studenthome/')
       return render(request,'StudentHome.html')
    else:
         return render(request,'StudentRegistraion.html')
def Studentview(request):
    details = TrainerAddDetails.objects.all()
    return render(request,'StudentView.html',{"eventz": details})
def studentprofile(request):
    return render(request,'StudentProfile.html')
def studentapplication(request):
    jobz=Companyjobpost.objects.all()
    return render(request,'StudentApplication.html',{"Student":jobz})
 