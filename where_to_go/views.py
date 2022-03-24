import os

from functools import reduce
from django.shortcuts import render

from places.models import Place


def render_main_page(request):
    places = Place.objects.all()
    places_details = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coordinates_lng, place.coordinates_lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": reduce(
                    os.path.join,
                    ['static', 'places', place.feature_filename])
                }
            }
        places_details['features'].append(feature)

    context = {"places_details": places_details}
    return render(request, 'index.html', context)
