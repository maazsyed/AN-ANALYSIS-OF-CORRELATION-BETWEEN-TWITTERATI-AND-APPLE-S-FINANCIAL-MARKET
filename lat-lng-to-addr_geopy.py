#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from geopy import geocoders
import sys, traceback

def latlng_to_addr (lat, lng):
    geocoder = geocoders.googlev3.GoogleV3()
    place, point = geocoder.geocode('%s,%s' % (lat, lng))
    return place

def main (argv):
    if len(argv) < 3:
        print ('usage: ./%s <lat> <lng>' % argv[0])
        exit(1)

    lat, lng = argv[1], argv[2]
    formatted_address = latlng_to_addr(lat, lng)
    print (formatted_address)


if __name__ == '__main__':
    #main(sys.argv)
    print(latlng_to_addr(52.5170365, 13.3888599))
