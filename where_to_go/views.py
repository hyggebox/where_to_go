from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def get_place_details(place):
    return {
        "title": place.title,
        "imgs": [img.image.url for img in place.image.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.coordinates_lng,
            "lat": place.coordinates_lat
        }
    }


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
                "detailsUrl": reverse('place-details',
                                      kwargs={'place_id':place.pk}),
                }
            }
        places_details['features'].append(feature)

    context = {"places_details": places_details}
    return render(request, 'index.html', context)


def render_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return JsonResponse(get_place_details(place),
                        safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
