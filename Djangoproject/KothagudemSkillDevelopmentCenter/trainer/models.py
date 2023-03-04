from django.db import models
Gender=(
    ('M','Male'),
    ('F','Female')
)

# Create your models here.
class TrainerAddDetails(models.Model):
    Title=models.TextField(max_length=120)
    TrainerName=models.TextField(max_length=120)
    TrainerDetails=models.TextField(max_length=120)
    Requirement=models.TextField(max_length=120)
    Date = models.DateField(auto_now=True)
    def __str__(self):
        return self.Title

class  TrainerRegistration(models.Model):
    name=models.TextField(max_length=120)
    email=models.EmailField(max_length=120)
    number=models.IntegerField()
    adderss=models.TextField(max_length=120)
    password=models.CharField(max_length=120)
    Gender=models.CharField(choices=Gender,max_length=120,default='male')
    def __str__(self):
        return self.name
        

class TrainerCredits(models.Model):
    Title=models.TextField(max_length=120)
    TrainerName=models.TextField(max_length=120)
    TrainerDetails=models.TextField(max_length=120)
    Requirement=models.TextField(max_length=120)
    Date = models.DateField(auto_now=True)
    def __str__(self):
        return self.Title
    