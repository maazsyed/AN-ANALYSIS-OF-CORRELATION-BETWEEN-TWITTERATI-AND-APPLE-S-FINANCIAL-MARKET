from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
geolocator = Nominatim()

import csv
count = 2
latitudeLongtitude = []
#latitudeLongtitude = [str(42.34234234)+","+str(-24.23442)]
with open('S:\Files\MASTERS\social medial mining\projects\Geo_data_30.csv', encoding="Latin-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        locationToGeocode = row['geo'] + row['country']
        try:
            location = geolocator.geocode(locationToGeocode, timeout=10)
            if location is not None:
                #print(location.latitude, location.longitude)
                latitudeLongtitude.append(str(location.longitude) +","+ str(location.latitude))
                #print(locationToGeocode, location.address)
                print(count)
                count += 1
        except GeocoderTimedOut as e:
            print("Error: geocode failed on input %s with message %s"%(locationToGeocode, e.msg))

print('eqfeed_callback({"type":"FeatureCollection","features":[')
for ll in latitudeLongtitude:
    print('{"geometry":{"type":"Point","coordinates":[', ll, ']}},')
print(']});')