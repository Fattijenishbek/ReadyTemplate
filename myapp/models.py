from django.db import models

# Create your models here.
class Features(models.Model):
    name = models.CharField(max_length=50) # it means the type is str with length
    details = models.CharField(max_length=200)