from django.http import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate,login
from . models import TrainerAddDetails
from . models import TrainerCredits
from . models import TrainerRegistration
# Create your views here.
def trainerlogin(request):
    if request.method=='POST':
      name=request.POST['tid']
      pas=request.POST['tpd']
      newuser=authenticate(username=email,password=password)
      if newuser is not None:
        login(request,newuser)
      return HttpresopnseRedirect('/trainerhome/')
      return render(request,'Trainerhome.html') 
    else: 
      return render(request,'TrainerLogin.html')
def trainerhome(request):
    return render(request,'Trainerhome.html')
def Trainerregistration(request):
    if request.method=='POST':
       Name=request.POST['tname']
       ema= request.POST['te']
       num=request.POST['tnum']
       add=request.POST['tad']
       pas=request.POST['tpd']
       gender=request.POST['tgender']
       jhon=TrainerRegistration(name=Name,email=ema,number=num,adderss=add,password=pas,Gender=gender)
       jhon.save()
       newuser=authenticate(username=ema,password=pas)
       if newuser is not None:
        login(request,newuser)
        return HttpResopnseRedirect('/trainerhome/')
       return render(request,'Trainerhome.html')
    else:
        return render(request,'TrainerRegistration.html')

def trainerviewall(request):
    details = TrainerAddDetails.objects.all()  
    return render(request,'TrainerViewall.html',{"Details": details})
def trainerprofile(request):
    return render(request,'TrainerProfile.html')
def traineradddetails(request):
    if request.method=='POST':
        ftitle = request.POST['title']
        fname = request.POST['tn']
        fdetails = request.POST['td']
        frequirement = request.POST['tr']
        addDetails = TrainerAddDetails(Title=ftitle,TrainerName=fname,TrainerDetails=fdetails,Requirement=frequirement)
        addDetails.save()
        details = TrainerAddDetails.objects.all()
        return render(request,'Traineradddeatils.html',{"Details": details})
    else:
        details = TrainerAddDetails.objects.all()
        return render(request,'Traineradddeatils.html',{"Details": details})
def trainercredits(request):
    if request.method=='Post':
        title=request.Post['title1']
        tname=request.Post['tname']
        tdetails=request.Post['tdetails']
        trequirement=request.Post['require']
        tcredits=request.Post['tdetials']
        fcredits = TrainerCredits( Title= title,TrainerName=tname,TrainerDetails= tdetails,Requirement=trequirement)
        fcredits.save()
        return render (request,'Trainercredits.html')
    else:
        credit = TrainerAddDetails.objects.all()
        return render (request,'Trainercredits.html',{"creditz":credit})

def deletetrainer(request,id):
    deletetrainerdetails = TrainerAddDetails.objects.get(id=id)
    deletetrainerdetails.delete()
    return render(request,'Trainerhome.html')
