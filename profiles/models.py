from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse # new


class UserProfile(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length=200)
    jobTitle= models.CharField(max_length =200)
    jobNumber= models.CharField(max_length =200, default = 'NA')
    basicPay =  models.DecimalField(max_digits=10, decimal_places=2)
    allowances =  models.DecimalField(max_digits=10, decimal_places=2, default='0000000', editable = True)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default='0000000', editable  = True)
    # logo = models.ImageField(upload_to='photos/', null=True, blank=True) # new

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): # new
        return reverse('profile_detail', args=[str(self.id)])

