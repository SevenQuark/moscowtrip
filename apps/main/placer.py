# -*- coding: utf-8 -*-
import foursquare

client = foursquare.Foursquare(
    client_id='BJ3NANVVRNF5RIQCPVTORRCV13UHCPAVYK1EF5S43OK0MAA2',
    client_secret='LJ5PJUZLQEISC1N0SFP5VWF35I5WJYDZR3BYCGGENXECAVON'
)


def get_places(categoryId):
    places = client.venues.search(params={'categoryId': categoryId, 'intent': 'browse', 'near': 'Moscow', 'limit': 50})
    return places['venues']