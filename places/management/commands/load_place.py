import json
import os
import sys
from urllib.parse import quote, urlparse

import requests
import validators
from django.core.management import BaseCommand
from django.core.files.base import ContentFile
from requests import JSONDecodeError

from places.models import Image, Place


def save_place(place_data):
    place, created = Place.objects.get_or_create(
        title=place_data['title'],
        defaults={
            'description_short': place_data['description_short'],
            'description_long': place_data['description_long'],
            'coordinates_lng': place_data['coordinates']['lng'],
            'coordinates_lat': place_data['coordinates']['lat']
        }
    )
    print('created =', created)
    return place


def save_images(place, img_urls):

    for image_url in img_urls:
        image_name = os.path.basename(urlparse(image_url).path)
        img_name_without_ext, ext = os.path.splitext(image_name)
        uploaded_images_names = [str(image.image) for image in place.images.all()]

        if any(img_name_without_ext in name for name in uploaded_images_names):
            continue
        response = requests.get(image_url)
        response.raise_for_status()

        image = Image()
        image.image.save(
            image_name,
            ContentFile(response.content),
            save=False
        )
        image.place = place
        image.save()


def is_file_path(string):
    if os.path.isfile(string):
        return string
    raise ValueError()


def is_url(string):
    if validators.url(string):
        return string
    raise ValueError()


class Command(BaseCommand):
    help = 'load place details from .json file to DB'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--local_path',
                            type=is_file_path,
                            help='Local path to a .json file with place details')
        parser.add_argument('-u', '--url',
                            type=is_url,
                            help='Url to a .json file with place details')

    def handle(self, *args, **options):
        local_path = options['local_path']
        url_to_place_data = options['url']

        if local_path:
            with open(local_path, encoding='utf8') as file:
                place_data = json.load(file)

        if url_to_place_data:
            response = requests.get(url_to_place_data)
            response.raise_for_status()
            try:
                place_data = response.json()
            except JSONDecodeError:
                sys.exit('Invalid data got from the URL')

        try:
            place_instance = save_place(place_data)
        except Exception as error:
            print(error)
        else:
            place_images_urls = place_data['imgs']
            save_images(place_instance, place_images_urls)
