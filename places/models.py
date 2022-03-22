from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates_lng = models.DecimalField(max_digits=16, decimal_places=14)
    coordinates_lat = models.DecimalField(max_digits=16, decimal_places=14)

    def __str__(self):
        return self.title