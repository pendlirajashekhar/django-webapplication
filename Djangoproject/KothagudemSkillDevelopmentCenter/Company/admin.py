from django.contrib import admin
from . models import companyregistration
from . models import Companyjobpost

# Register your models here.
admin.site.register(companyregistration)
admin.site.register(Companyjobpost)