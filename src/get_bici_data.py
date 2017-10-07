#!/usr/bin/env python3
#****************************************************************************#
# Project: Smart Jump                                                        #
# Author: Alfonso Bilbao Velez <alfon.linux@gmail.com>                       #
# Developed: Hackatinho Mobilidade Sostible                                  #
# License: AGPL                                                              #
#****************************************************************************#

# MODULO BICI CORUNHA #
# Librerias #
import os
import sys
import requests
import json

# Ficheros #
f1 = open("dataset/ubicacion_estaciones_bici.json", "w")
f2 = open("dataset/estado_estaciones_bici.json", "w")

# Header #
headers = {'x-sofia2-apikey': "14b0fdf8d58541a087c49a97f61903eb",
           'content-type': "application/json;charset=utf-8",
          }

# Estaciones de BiciCorunha con sus ubicaciones #
"""Fetch backstations."""
def ubicacion_estaciones():
    ubicacion_estaciones = "https://smart.coruna.es/sib-api/api/v1/openDataBiciCoruna/getAssets"
    u1 = requests.get(ubicacion_estaciones, headers=headers)
    u1_json = u1.json()
    print(json.dumps(json.loads(u1_json['data'])), file=f1)
    # json.dump(f1,json.loads(u1_json['data']))

# Estado de las diferentes estaciones de BiciCorunha #
def estado_estaciones():
    estado_estaciones = "https://smart.coruna.es/sib-api/api/v1/openDataBiciCoruna/getMeasures"
    e1 = requests.get(estado_estaciones, headers=headers)
    e1_json = e1.json()
    print(json.dumps(json.loads(e1_json['data'])), file=f2)
    # json.dump(f2,json.loads(e1_json['data']))

def main():
    # Ubicacion estaciones de bici.
    ubicacion_estaciones()

    # Estado de las estaciones de bici.
    estado_estaciones()

if __name__=='__main__':
    main()

