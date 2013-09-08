import datetime
import math

def group_data(start_date, end_date):
    import pymongo
    con = pymongo.MongoClient()
    db = con.instagram
    col = db.activities

    current_day = start_date
    res = {}
    days_diff = (end_date - start_date).days
    for day in range(0, days_diff):
        day_activity = col.find({'date': {'$gte': current_day, '$lt': current_day + datetime.timedelta(days=1)}})

        for doc in day_activity:
            fid = doc['fid']

            if fid not in res:
                res[fid] = {'days': [0 for x in range(0, days_diff)]}

            res[fid]['days'][day] += 1
        current_day += datetime.timedelta(days=1)

    return res


def norm(days_list, max_val):
    return [int(round(float(math.log(day + 1))*2 / math.log(max_val + 1))) + 1 for day in days_list]


def get_norm_activities_by_days(start_date, end_date):
    start_date = datetime.datetime.strptime('01.07.2013', '%d.%m.%Y')
    end_date = datetime.datetime.strptime('08.07.2013', '%d.%m.%Y')
    days_by_fid = group_data(start_date, end_date)

    res = []
    max_day_value = 0
    for fid, data in days_by_fid.items():
        temp_max = max(data['days'])
        if temp_max > max_day_value:
            max_day_value = temp_max

    for fid, data in days_by_fid.items():
        res.append({'fid': fid, 'days':norm(data['days'], max_day_value) })


    print res


# get_norm_activities_by_days(None, None)