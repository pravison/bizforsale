from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class CommercialRealEState(models.Model):
    title = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    listedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    askingPrice = models.CharField(max_length=150)
    propertyName = models.CharField(max_length=200)
    owner = models.TextField(max_length=300)
    totalRooms = models.CharField(max_length=100)
    currentOccupiedRooms = models.CharField(max_length=100)
    averageMontlyRentalIncome = models.CharField(max_length=100)
    propertyDescription = models.TextField(blank=True, null=True)
    numberOfWorkers = models.IntegerField(default=0)

    roomPhotos1 = models.EmailField(blank=True, null=True)
    roomPhotos2 = models.EmailField(blank=True, null=True)
    roomPhotos3 = models.EmailField(blank=True, null=True)
    roomPhotos4 = models.EmailField(blank=True, null=True)
    roomPhotos5 = models.EmailField(blank=True, null=True)
    roomPhotos6 = models.EmailField(blank=True, null=True)

    titleDeadExists = models.BooleanField(default=False) 
    propertySquareArea = models.CharField(max_length=100, blank=True, null=True)
    propertyBluePrints = models.BooleanField(default=False)
    constructedOn = models.DateField(blank=True, null=True)

    propertyDisputes= models.BooleanField(default=False)
    disputesDescription = models.TextField(blank=True, null=True)
    repairNeeded = models.BooleanField(default=False)
    repairDescription = models.TextField(blank=True, null=True)

    country = models.CharField(max_length=150)
    county =models.CharField(max_length=150)
    locationn = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    featured = models.BooleanField(default=False)
    closed_deal = models.BooleanField(default=False) 

    def __str__(self):
        return self.title



