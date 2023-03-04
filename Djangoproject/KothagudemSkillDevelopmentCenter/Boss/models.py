from django.db import models

# Create your models here.
class AdminEventAdd(models.Model):
     eventName=models.TextField(max_length=120)
     TrainerName=models.TextField(max_length=120)
     Requirment=models.TextField(max_length=120)
     messeage=models.TextField(max_length=120)
     EventDate=models.DateField()
     Location=models.TextField(max_length=120)
     Status=models.TextField(max_length=12,default="Open")
     def __str__(self):
        return self.eventName +'----'+ self.TrainerName +'----'+self.Location
        
