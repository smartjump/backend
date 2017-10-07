#!/usr/bin/env python3
#****************************************************************************#
# Project: Smart Jump                                                        #
# author: nixijav <nixijav@nixijav.com>                                      #
# author: alfonso bilbao velez <alfon.linux@gmail.com>                       #
# Developed: Hackatinho Mobilidade Sostible                                  #
# License: AGPL                                                              #
#****************************************************************************#

# MODULO CALCULATE DISTANCE #
# Librerias #
import json
import operator
from math import acos
from math import cos
from math import sin
from math import radians


def haversine(lat_parada, lon_parada, lat_usuario, lon_usuario):
    distancia = 6371000 * acos(cos(radians(lat_parada)) * cos(radians(lat_usuario)) *\
    cos(radians(lon_usuario) - radians(lon_parada)) +\
    sin(radians(lat_parada)) * sin(radians(lat_usuario)))

    return distancia

def calculate_distance(lat_usuario, lon_usuario):
    jumps = open("dataset/get_jumps.json", "r")
    jumps_data = json.load(jumps)

    data_out = []
    for i,elem in enumerate(jumps_data):
        latitude = float(elem['lat'])
        longitude = float(elem['lon'])
        distancia = haversine(latitude , longitude, lat_usuario,\
            lon_usuario)
        nome = elem['assetName']
        ids = elem['assetId']
        bicis = elem['available']
        data_out.append({'id':ids, 'latitude':latitude,
            'longitude':longitude, 'distance':distancia, 'mean':"bike",
            'info':{'addres': nome,'available':bicis}})

    #print(data_out)
    data_out.sort(key=operator.itemgetter('distance'))

    return data_out



