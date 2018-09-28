# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:44:34 2018

@author: Andres
"""
import DataClean as dc
import pandas as pd
from twitter import *
try:
    import json
except ImportError:
    import simplejson as json
#from TwitterSearch import TwitterSearchOrder, TwitterSearchException

# Credenciales adquiridad en aplicaciones de Twitter
token='392438580-NY53JVkA8OvIVeZU6x7peQO98RMe7Jdmn0lo6Wdu'
token_secret='kHcKfg1Dxjps5UpgfBQEZM3PZ1ucq9QF4SM0GheTSzVUi'
consumer_key='aHrevgsaE7LQFnmE5MRD3WMOr'
consumer_secret='d32tTQW33ecgIVaJjqFtwqjHmNpdyEw1TCiWVo5V0OxVZvenjD'

# Se inicializa la variable con las credenciales con el fin de poder hacer búsquedas
t = Twitter(
    auth=OAuth(token, token_secret,consumer_key,consumer_secret))

# Toma el arreglo de terminos y los pone en el formato admitido por API Twitter
def separateParameters(setParamenters):
    chainSearch=''
    for i in range(len(setParamenters)):
        chainSearch+=detectSpace(setParamenters[i])
        chainSearch+=' '
    return chainSearch


# Detecta las frases que son incluidas en los términos
def detectSpace(wordText):
    if (' ' in wordText) == True:
        return '"'+wordText+'"'
    else:
        return wordText

# Genera el dataframe final tratando los datos, además utiliza disyunción lógica
def generarCompendioOR(listaPalabras,listaFechas,typeFilter):
    arrFinal=[]
    estadoConsulta=True
    for i in range(len(listaPalabras)):
        for j in range(len(listaFechas)):
            consulta=t.search.tweets(q=listaPalabras[i],count=100,result_type=typeFilter,lang='es',until=listaFechas[j],tweet_mode='extended')
            extConsulta=consulta['statuses']
            if(extConsulta==[]):
                print(f'El termino: {listaPalabras[i]}  y la fecha {listaFechas[j]} no arrojo resultado')
            else:
                dataFrameGenerado=dc.tratamientoDeDatos(extConsulta)
                arrFinal.append(dataFrameGenerado)
    if arrFinal == []:
        dataFrameCompendio=[]
        estadoConsulta=False
    else:
        dataFrameCompendio=pd.concat(arrFinal,axis=0,ignore_index=True)
    return dataFrameCompendio, estadoConsulta

# Genera el dataframe final tratando los datos, además utiliza conjunción lógica
def generarCompendioAND(listaPalabras,listaFechas,typeFilter):
    arrFinal=[]
    estadoConsulta=True
    for j in range(len(listaFechas)):
        consulta=t.search.tweets(q=listaPalabras,until=listaFechas[j],lang='es',count=100,result_type=typeFilter,tweet_mode='extended')
        extConsulta=consulta['statuses']
        if(extConsulta==[]):
            print(f'El termino: {listaPalabras} y la fecha {listaFechas[j]} no arrojo resultado')
        else:
            dataFrameGenerado=dc.tratamientoDeDatos(extConsulta)
            arrFinal.append(dataFrameGenerado)
    if arrFinal == []:
        dataFrameCompendio=[]
        estadoConsulta=False
    else:
        dataFrameCompendio=pd.concat(arrFinal,axis=0,ignore_index=True)
    return dataFrameCompendio, estadoConsulta
