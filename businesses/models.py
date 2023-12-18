from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Industry(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class information(models.Model):
    choices= [
        'owned','owned', 
        'leased','leased'
        ]
    
    title = models.TextField(max_length=150)
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    asking_price = models.CharField(max_length=150)
    business_name = models.CharField(max_length=150)
    business_owner =  models.CharField(max_length=150)
    business_photo = models.ImageField()
    cashflow = models.CharField(max_length=150)
    gross_annual_revenue = models.CharField(max_length=150)
    profits = models.CharField(max_length=150)

    country = models.CharField(max_length=150)
    county =models.CharField(max_length=150)
    locationn = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    realestate = models.Choices()
    lease_expiration =models.DateField(blank=True, null=True)
    inventory = models.TextField(blank=True, null=True)
    number_of_employes = models.IntegerField(default=0)

    description = models.TextField(blank=True, null=True)
    competion = models.TextField(blank=True, null=True)
    support_and_training = models.TextField(blank=True, null=True)

    featured = models.BooleanField(default=False)
    closed_deal = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

