import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Location: ')
    if len(address) < 1: break

url = serviceurl + urllib.urlparse.urlencode(
    {'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
date = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = None

    if not js or 'status' in js or js['status'] != 'OK':
        print('==== Failure to Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
