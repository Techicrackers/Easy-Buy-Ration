from django.db import models

# Create your models here.
class product(models.Model):
    productname=models.CharField(max_length=20, default="")
    quantity=models.CharField(max_length=20, default="")
    price=models.IntegerField()
    def __str__(self):
        return self.productname
class customers(models.Model):
    name=models.CharField(max_length=20, default="")
    productname = models.CharField(max_length=20, default="")
    aadhaarnumber=models.BigIntegerField()
    gender=models.CharField(max_length=20, default="")
    members=models.CharField(max_length=20, default="")
    dob=models.CharField(max_length=20, default="")
    cardnumber=models.IntegerField(default="")
    phone=models.BigIntegerField()
    Mail=models.CharField(max_length=20, default="")
    password=models.IntegerField()
    cardtype=models.CharField(max_length=20, default="")
    def __str__(self):
        return self.name
class transaction(models.Model):
    name=models.CharField(max_length=20, default="")   
    transactionid = models.IntegerField(default="")
    date=models.CharField(max_length=20, default="")
    time=models.CharField(max_length=20, default="")
    amount=models.IntegerField(default="")
    customername=models.CharField(max_length=20, default=0)
