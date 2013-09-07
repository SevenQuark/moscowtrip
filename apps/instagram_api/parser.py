import datetime
import pymongo
import httplib
import json


con = pymongo.MongoClient()
db = con.instagram
col = db.activities
col_instagram_ids = db.instagram_ids

main_url = 'api.instagram.com'
api_url = '/v1/locations/%s/media/recent?min_timestamp=%s&max_timestamp=%s&access_token=239714484.6654a78.1f76288cc8bf4004a64356023d5d7830'
max_id = 'max_id=%s'
get_instagram_id_url = '/v1/locations/search?foursquare_v2_id=%s&access_token=239714484.6654a78.1f76288cc8bf4004a64356023d5d7830'

start_date = 1372636800
end_date = 1373241600


def save_data(data, iid, fid, category):
    all_obj = data['data']

    for d in all_obj:
        date = datetime.datetime.fromtimestamp(int(d['created_time']))
        aid = d['id']

        col.save({'_id': aid, 'iid': iid, 'date': date, 'fid': fid, 'category': category})


def parse_activities(iid, fid, category, next_max_id):
    conn = httplib.HTTPSConnection(main_url)
    url = api_url % (iid, start_date, end_date)
    if next_max_id:
        url += '&' + max_id % next_max_id
    conn.request("GET", url)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    json_data = r1.read()
    data1 = json.loads(json_data)
    save_data(data1, iid, fid, category)
    if data1['pagination'] and 'next_max_id' in data1['pagination']:
        parse_activities(iid, fid, category, data1['pagination']['next_max_id'])


def get_instagram_id(fid, category):
    conn = httplib.HTTPSConnection(main_url)
    url = get_instagram_id_url % fid
    conn.request("GET", url)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    json_data = r1.read()
    data1 = json.loads(json_data)
    iid = data1['data'][0]['id']
    col_instagram_ids.save({'_id': fid, 'iid': iid, 'latitude': data1['data'][0]['latitude'], 'longitude': data1['data'][0]['longitude'], 'category': category})
    return iid


def add_places(all_places):
    for place in all_places:
        fid = place.place_id
        category = place.category
        print fid
        iid_doc = col_instagram_ids.find_one({'_id': fid})

        if not iid_doc:
            iid = get_instagram_id(fid, category)
        else:
            iid = iid_doc['iid']

        if not col.find_one({'iid': iid}):
            print 'parse', iid
            parse_activities(iid, fid, category, None)

