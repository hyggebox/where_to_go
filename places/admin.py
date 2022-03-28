from django.contrib import admin

from places.models import Place, Image



class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    ordering = ('position',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'place')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]