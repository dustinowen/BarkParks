from django.db import models

RATINGS = (
    (5, '5-Stars'),
    (4, '4-Stars'),
    (3, '3-Stars'),
    (2, '2-Stars'),
    (1, '1-Star'),
)

# Create your models here.
class DogParks(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    LAT = models.DecimalField(max_digits=9, decimal_places=6)
    LON = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    date = models.DateField()
    rating = models.IntegerField(
        choices=RATINGS, 
        default=RATINGS[0][0]
    )
    park = models.ForeignKey(DogParks, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()}"

