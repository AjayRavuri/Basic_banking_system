from django.db import models

# Create your models here.
class Customer(models.Model):
    cname=models.CharField(max_length=64)
    accno=models.CharField(max_length=64)
    acctype=models.CharField(max_length=64)
    mail=models.CharField(max_length=64)
    cbal=models.FloatField()
class Transaction(models.Model):
    sname=models.CharField(max_length=64)
    saccno=models.CharField(max_length=64)
    rname=models.CharField(max_length=64)
    raccno=models.CharField(max_length=64)
    amnt=models.FloatField()
