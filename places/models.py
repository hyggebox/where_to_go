from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates_lng = models.DecimalField(max_digits=16, decimal_places=14)
    coordinates_lat = models.DecimalField(max_digits=16, decimal_places=14)
    feature_filename = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='')
    place = models.ForeignKey('Place',
                             related_name='image',
                             on_delete=models.CASCADE,
                             null=True)

    def __str__(self):
        return f'Картинка id {self.id}'
