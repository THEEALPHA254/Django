from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.BigIntegerField()
    email_address = models.EmailField(max_length=23)
    date_of_reg = models.DateField(auto_now=True)

class Hostels(models.Model):
    hostel_name = models.CharField(max_length=100)
    hostel_type = models.CharField(max_length=100)
    no_of_occupants = models.IntegerField()

class HostelAllocation(models.Model):
    hostel_allocation = models.BooleanField(auto_created=True)
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostels, on_delete=models.CASCADE)