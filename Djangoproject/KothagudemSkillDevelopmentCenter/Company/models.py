from django.db import models
Gender=(
    ('M','Male'),
    ('F','Female')
)


# Create your models here.

class companyregistration(models.Model):
    name=models.TextField(max_length=120)
    email=models.EmailField(max_length=120)
    number=models.TextField(max_length=120)
    adderss=models.TextField(max_length=120)
    password=models.CharField (max_length=120)
    Gender=models.CharField(choices=Gender,max_length=120,default='male')
    image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name +'----'+ self.email +'----'+self.adderss + '-----' +self.password
        
    
class Companyjobpost(models.Model):
    companyName=models.TextField(max_length=120)
    description=models.TextField(max_length=120)
    Requrirement=models.TextField(max_length=120)
    Requirementdetails=models.TextField(max_length=120)
    Creditcheck=models.TextField(max_length=120)  
    def __str__(self):
        return self. companyName +'-----'+ self.description + '----'+self.Requrirement
        