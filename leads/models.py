from django.db import models
from django.contrib.auth.models import User
 

# Create your models here.
class Leads(models.Model):
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True)
    target_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    
class Newsletter(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.full_name