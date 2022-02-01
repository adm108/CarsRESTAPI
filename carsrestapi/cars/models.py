from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    @property
    def avg_rating(self):
        if self.ratings.aggregate(avg_rating = Avg('rate'))['avg_rating'] != None:
            return round(self.ratings.aggregate(avg_rating = Avg('rate'))['avg_rating'], 1)
        return self.ratings.aggregate(avg_rating = Avg('rate'))['avg_rating']
    
    class Meta:
        unique_together = ('make', 'model',)
        verbose_name_plural = 'Cars'


class Rating(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='ratings')
    rate = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        verbose_name_plural = 'Ratings'
