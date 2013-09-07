# -*- coding: utf-8 -*-
import foursquare
import datetime
import calendar


client = foursquare.Foursquare(
    client_id='BJ3NANVVRNF5RIQCPVTORRCV13UHCPAVYK1EF5S43OK0MAA2',
    client_secret='LJ5PJUZLQEISC1N0SFP5VWF35I5WJYDZR3BYCGGENXECAVON',
    redirect_uri='http://moscowtrip.travelatus.com'
)
# auth_uri = client.oauth.auth_url()
# client.set_access_token('NJE44TA0DXD0D0Z53F5DAJWWGOEBQUKMXCK2FUHDMDLTGDRP')
# user = client.users()
# print(user)

def update_stat(place):
    start_at = datetime.datetime(2013, 8, 11)
    end_at = datetime.datetime(2013, 8, 17)
    start_at = calendar.timegm(start_at.utctimetuple())
    end_at = calendar.timegm(end_at.utctimetuple())

    return client.venues.GET('timeseries', params={
            'venueId': place.place_id, 'startAt': start_at, 'endAt': end_at
        }, multi=False)


def places():
    result = []
    places = Place.objects.all()
    for p in places:
        result.append(dict(
            place=p.data,
            category='',
            population=0
        ))
    return result


def get_places(categoryId='4bf58dd8d48988d163941735'):
    places = client.venues.search(params={'categoryId': categoryId, 'intent': 'browse', 'near': 'Moscow', 'limit': 50})
    return places['venues']


def update():
    from apps.main.models import Place
    places = get_places('4bf58dd8d48988d181941735')  # Парки
    for place in places:
        Place.objects.get_or_create(place_id=place['id'], defaults={
            'data': place,
            'category': 'museum'
        })
