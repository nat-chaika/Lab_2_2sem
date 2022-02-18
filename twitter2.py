from distutils.log import info
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import folium
from geopy.geocoders import Nominatim

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
def twitter(acct):
    """
    Innitual function
    Gets Twitter API with keys from hidden.py
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    # acct = input('Enter Twitter Account:')
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '200'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    # with open("content.json", "w", encoding='utf-8') as filyk:
    #     json.dump(js, filyk, indent=2)
    # inf = json.dumps(js, indent=2)
    
    return js


def get_locations(data):
    """
    Gets names and locations from info
    """
    users = data.get("users")
    accounts = []
    for acc in users:
        name = acc["screen_name"]
        location = acc["location"]
        accounts.append([name, location])
    return accounts


def find_locations(accounts):
    """
    Finds dots on the map, creates map
    """
    map = folium.Map(location=[41.881832, -87.623177],
                    zoom_start = 1)
    fg = folium.FeatureGroup(name = 'friends')
    loc = Nominatim(user_agent="GetLoc")
    for i in accounts:
        name = i[1]
        try:
            getLoc = loc.geocode(name)
            lt = getLoc.latitude
            ln = getLoc.longitude
            fg.add_child(folium.Marker(location=[lt, ln],
            popup = i[0],
            icon = folium.Icon()))
        except: pass
    map.add_child(fg)
    map.add_child(folium.LayerControl())
    map.save('templates/Map_friends.html')
    return True

def do_the_map(acct):
    """
    Main function
    """
    inf = twitter(acct)
    find_locations(get_locations(inf))
    return True