from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Adminlogin(request):
    return render(request,'AdminLogin.html')
def Adminhome(request):
    return render(request,'Adminhome.html')
def Adminviewall(request):
    return render(request,'AdminViewall.html')
def AdminEventadd(request):
    return render(request,'AdminEventadd.html')
def Adminprofile(request):
    return render(request,'AdminProfile.html')
def Adminapprover(request):
    return render(request,'Adminappover.html')
