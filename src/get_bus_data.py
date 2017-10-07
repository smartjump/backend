#!/usr/bin/env python3
#****************************************************************************#
# Project: Smart Jump                                                        #
# Author: Alfonso Bilbao Velez <alfon.linux@gmail.com>                       #
# Developed: Hackatinho Mobilidade Sostible                                  #
# License: AGPL                                                              #
#****************************************************************************#

# MODULO BUS CORUNHA #
# Librerias #
import os
import sys
import requests
import json

# Ficheros #
f1 = open("dataset/ubicacion_paradas_bus.json", "w")
f2 = open("dataset/info_por_parada.json", "w")

# Header #
headers = {'x-sofia2-apikey': "14b0fdf8d58541a087c49a97f61903eb",
           'content-type': "application/json;charset=utf-8",
          }

# Estaciones de Bus Corunha con sus ubicaciones #
"""Fetch backstations."""
def ubicacion_paradas():
    ubicacion_paradas = "https://smart.coruna.es/sib-api/api/v1/openDataParadaAutobus/getAssets"
    u1 = requests.get(ubicacion_paradas, headers=headers)
    u1_json = u1.json()
    print(json.dumps(json.loads(u1_json['data'])), file=f1)
    # json.dump(f1, json.loads(u1_json['data']))


# Toda la info de una parada de autobus urbano.
def info_parada():
    for i in range(1,50):
        info_parada =\
        "https://smart.coruna.es/sib-api/api/v1/openDataParadaAutobus/getAssetInfo?$id=%d" %i
        p1 = requests.get(info_parada, headers=headers)
        p1_json = p1.json()
        print(json.dumps(json.loads(p1_json['data'])), file=f2)


def main():
    # Ubicacion paradas de bus.
    ubicacion_paradas()
    info_parada()

if __name__=='__main__':
    main()

