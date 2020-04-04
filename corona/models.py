from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

HELPS =(
    ('Medical','Medical Help'),
    ('Food','Food Related Issues'),
    ('police','Police Help'),
    ('safety','Safety Issues'),
    ('other','Others'),
)

class District(models.Model):
    dName = models.CharField(max_length=100)

    def __str__(self):
        return self.dName

class Hospitals(models.Model):
    hName = models.CharField(max_length=100)
    #hContact = models.IntegerField(null=True)
    state = models.ForeignKey(District,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.hName


class rescue(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField(max_length=100,null=True)
    pincode = models.IntegerField()
    user_phone = PhoneNumberField(null=False, blank=False, unique=True, default='+91')

    def __str__(self):
        return self.name


# Emergency contact

class contact(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    typeHelp = models.CharField(max_length=50,choices=HELPS,default='Medical Help')
    phone = PhoneNumberField(null=False,blank=False,unique=True,default='+91')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


