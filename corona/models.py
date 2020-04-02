from django.db import models

# Create your models here.

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