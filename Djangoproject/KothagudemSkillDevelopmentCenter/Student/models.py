from django.db import models
Gender=(
    ('M','Male'),
    ('F','Female')
)

# Create your models here.
class  StudentRegistration(models.Model):
    name=models.TextField(max_length=120)
    email=models.EmailField(max_length=120)
    number=models.TextField(max_length=120)
    adderss=models.TextField(max_length=120)
    password=models.CharField (max_length=120)
    Gender=models.CharField(choices=Gender,max_length=120,default='male')
    def __str__(self):
        return self.name
        