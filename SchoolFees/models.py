from django.db import models

# Create your models here.
class Fee_balance(models.Model):
    balance = models.IntegerField()
    student = models.ForeignKey('register.Students',on_delete=models.CASCADE)


class Fee_payments(models.Model):
    payment = models.IntegerField()
    student = models.ForeignKey('register.Students',on_delete=models.CASCADE)