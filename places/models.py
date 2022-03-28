from django.db import models
from django.utils.html import format_html


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
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
                              related_name='image',
                              on_delete=models.CASCADE,
                              null=True)
    position = models.PositiveIntegerField('Позиция', default=0,
                                           null=True, blank=True)

    def get_preview(self):
        return format_html('<img src="{url}" height={height}>'.format(
            url=self.image.url,
            height=200
        ))

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f'Картинка id {self.id}'
