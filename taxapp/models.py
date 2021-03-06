from django.db import models
import datetime

# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=255)
    tax_rate = models.CharField(max_length=10)
    def __unicode__(self):
        return (self.name)

class Zip_Code(models.Model):
    zip_code = models.CharField(max_length=5)
    county = models.ForeignKey(County)
    def __unicode__(self):
        return (self.zip_code)

class City(models.Model):
    name = models.CharField(max_length=255)
    zip_code = models.ManyToManyField(Zip_Code)
    def __unicode__(self):
        return (self.name)
