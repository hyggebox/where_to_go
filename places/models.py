from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=100, unique=True)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    coordinates_lng = models.DecimalField('Широта',
                                          max_digits=8, decimal_places=6)
    coordinates_lat = models.DecimalField('Долгота',
                                          max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Картинка', upload_to='')
    place = models.ForeignKey('Place',
                              verbose_name='Место',
                              related_name='images',
                              on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Позиция', default=0, blank=True)

    def get_preview(self):
        return format_html('<img src="{}" height={}>', self.image.url, 200)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['position']

    def __str__(self):
        return f'Картинка id {self.id}'
