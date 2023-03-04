from django.http import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate,login

from . models import Companyjobpost,companyregistration


# Create your views here.
def Companylogin(request):
    if request.method=='POST':
      name=request.POST['cid']
      pas=request.POST['cpd']
      newuser=authenticate(username=email,password=password)
      if newuser is not None:
        login(request,newuser)
      return HttpresopnseRedirect('/CompanyHome/')
      return render(request,'Company_home.html')  
    else:  
        return render(request,'Company_login.html')                                                       
def Companyregistration(request):
    if request.method=='POST':
       Name=request.POST['name']
       ema= request.POST['cem']
       num=request.POST['cnum']
       add=request.POST['cad']
       pas=request.POST['cppd']
       gender=request.POST['gender']
       img=request.POST['im']
       sand=companyregistration(name=Name,email=ema,number=num,adderss=add,password=pas,Gender=gender,image= img)
       sand.save()
       newuser=authenticate(username=ema,password=pas)
       if newuser is not None:
        login(request,newuser)
        return HttpResopnseRedirect('/CompanyHome/')
       return render(request,'Company_home.html')
    else:
        return render(request,'Company_Registration.html')
def Companyhome(request):
    return render(request,'Company_home.html')
def Companyapplicants(request):
    return render(request,'Companyapplicants.html')
def Companynotification(request):
    return render(request,'Companynotification.html')
def companyjobpost(request):
    if request.method=='POST':
        cname=request.POST['cnm']
        desc=request.POST['cd']
        req=request.POST['cr']
        reqd=request.POST['crd']
        credit=request.POST['ccheck']
        details=Companyjobpost(companyName=cname,description=desc,Requrirement=req,Requirementdetails=reqd,Creditcheck=credit)
        details.save() 
        jobz=Companyjobpost.objects.all()
        return render(request,'Company_home.html',{"Job":jobz})  
    else:
        jobz=Companyjobpost.objects.all()
        return render(request,'Company_jobpost.html',{"Job":jobz})
    
def companyprofile(request):
     return render(request,'Company_Profile.html')
    