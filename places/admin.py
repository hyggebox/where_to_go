from django.contrib import admin

from places.models import Place, Image

# Register your models here.
admin.site.register(Place)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'place')