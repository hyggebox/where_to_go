import os
from urllib.parse import quote, urlparse

import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from django.core.files.base import ContentFile

from places.models import Image, Place


def get_titles():
    repo_url = 'https://github.com/devmanorg/where-to-go-places/tree/master/places'
    response = requests.get(repo_url)
    response.raise_for_status()
    repo_soup = BeautifulSoup(response.text, 'html.parser')
    raw_titles = repo_soup.select('.js-navigation-item a.Link--primary')
    return [title.text for title in raw_titles]


def get_contents(title):
    base_url = 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/'
    response = requests.get(f'{base_url}{quote(title)}')
    response.raise_for_status()
    return response.json()


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
    return place


def save_images(place, img_urls):

    for image_url in img_urls:
        image_name = os.path.basename(urlparse(image_url).path)
        img_name_without_ext, ext = os.path.splitext(image_name)
        uploaded_images_names = [str(image.image) for image in place.image.all()]

        if not any(img_name_without_ext in name for name in uploaded_images_names):
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
        else:
            continue


def main():
    places_titles = get_titles()
    for title in places_titles:
        place_data = get_contents(title)
        place = save_place(place_data)
        place_images_urls = place_data['imgs']
        save_images(place, place_images_urls)


class Command(BaseCommand):

    def handle(self, *args, **options):
        main()
