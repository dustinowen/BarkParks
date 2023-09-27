from django.db import models

# Create your models here.
class DogParks(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    LAT = models.DecimalField(max_digits=9, decimal_places=6)
    LON = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
    
