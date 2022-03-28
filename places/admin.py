from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    ordering = ('position',)
    fields = ('image', 'get_preview', 'position')
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return obj.get_preview()

    get_preview.short_description = 'Превью'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'place', 'get_preview')
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return obj.get_preview()

    get_preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]