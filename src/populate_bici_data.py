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
import json
import pandas as pd

def main():
    # Ficheros #
    path = "dataset/get_jumps.json"
    ubicacion = open("dataset/ubicacion_estaciones_bici.json", "r")
    estado = open("dataset/estado_estaciones_bici.json", "r")
    
    # Datos #
    ubicacion_json_data = json.load(ubicacion)
    estado_json_data = json.load(estado)
    
    #datos1 = pd.read_json(ubicacion)
    #datos2 = pd.read_json(estado)
    
    # Redefinir el data frame.
    estados = [
            {
                'assetId': feed['Feed']['assetId'],
                'available':int(feed['Feed']['measures'][1]['measure']),
                'total':int(feed['Feed']['measures'][0]['measure']),
            } for feed in estado_json_data
              ]
    
    df_estados = pd.DataFrame(estados)
    
    df_ubicaciones = pd.io.json.json_normalize(ubicacion_json_data)
    df_ubicaciones['assetId'] = df_ubicaciones['Feed.assetId']
    
    del df_ubicaciones['Feed.assetId']
    
    df_lat = df_ubicaciones['Feed.geometry.coordinates'].map(lambda e: float(e[1]))
    df_lon = df_ubicaciones['Feed.geometry.coordinates'].map(lambda e: float(e[0]))
    
    # Latitud y Longitud.
    df_ubicaciones['lat'] = df_lat
    df_ubicaciones['lon'] = df_lon
    
    del df_ubicaciones['Feed.geometry.coordinates']
    
    df = pd.merge(df_estados, df_ubicaciones, on='assetId')
    df['assetId'] = df['assetId'].map(int)
    df = df.set_index('assetId', drop=False)
    df = df.sort_index()
    df = df.rename(columns={'Feed.assetName': 'assetName'})
    
    df.to_json(path, orient='records')
    
if __name__=='__main__':
    main()

