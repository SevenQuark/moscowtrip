# -*- coding: utf-8 -*-
import foursquare
from apps.main.models import Place

client = foursquare.Foursquare(
    client_id='BJ3NANVVRNF5RIQCPVTORRCV13UHCPAVYK1EF5S43OK0MAA2',
    client_secret='LJ5PJUZLQEISC1N0SFP5VWF35I5WJYDZR3BYCGGENXECAVON'
)


def places():
    result = []
    places = Place.objects.all()
    for p in places:
        result.append(p.data)
    return result


def get_places(categoryId):
    places = client.venues.search(params={'categoryId': categoryId, 'intent': 'browse', 'near': 'Moscow', 'limit': 50})
    return places['venues']


def update(categoryId):
    places = placer.get_places('4bf58dd8d48988d163941735')  # Парки
    for place in places:
        Place.objects.get_or_create(place_id=place['id'], defaults={
            'data': place
        })
