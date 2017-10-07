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

# Header #
headers = {'x-sofia2-apikey': "14b0fdf8d58541a087c49a97f61903eb",
           'content-type': "application/json;charset=utf-8",
          }

# Estaciones de Bus Corunha con sus ubicaciones #
"""Fetch backstations."""
def ubicacion_paradas():
    ubicacion_paradas = "https://smart.coruna.es/sib-api/api/v1/openDataParadaAutobus/getAssets"
    p1 = requests.get(ubicacion_paradas, headers=headers)
    p1_json = p1.json()
    print(json.dumps(json.loads(p1_json['data'])), file=f1)
    # json.dump(f1, json.loads(p1_json['data']))


def main():
    # Ubicacion paradas de bus.
    ubicacion_paradas()


if __name__=='__main__':
    main()

