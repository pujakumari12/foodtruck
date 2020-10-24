from django.db import models

# Create your models here.
class FoodTrucks(models.Model):
    truck_location = models.CharField(max_length=200)
    food_type = models.CharField(max_length=200)
    open_time = models.CharField(max_length=200)
    closing_time = models.CharField(max_length=200)
    