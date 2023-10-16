from django.db import models
from django.contrib.auth.models import User

RATINGS = (
    (5, '5-Stars'),
    (4, '4-Stars'),
    (3, '3-Stars'),
    (2, '2-Stars'),
    (1, '1-Star'),
)

class DogParks(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100, unique=True)
    hours = models.CharField(max_length=100, blank=True)

    users = models.ManyToManyField(User, related_name='saved_parks')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

    @classmethod
    def parks_added_by_user(cls, user):
        return cls.objects.filter(user=user)
    
class Reviews(models.Model):
    date = models.DateField('Review Date')
    rating = models.IntegerField('User Rating',
        choices=RATINGS, 
        default=RATINGS[0][0],
    )
    review = models.TextField(max_length=500, blank=True)
    park = models.ForeignKey(DogParks, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Pictures(models.Model):
    image = models.ImageField(upload_to='park_images/')
    date = models.DateField()
    description = models.CharField(max_length=100)

    park = models.ForeignKey(DogParks, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
