# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 23:47:04 2018

@author: Andres
"""
import pandas as pd
import numpy as np

# Función para obtener las palabras más repetidas
def wordsMoreRepetitive(dfFrecuenciaPalabras):
    palabrasRepetidas=dfFrecuenciaPalabras.head(5)
    x=palabrasRepetidas['PALABRA']
    y=palabrasRepetidas['FRECUENCIA']
    datosX=x.tolist()
    datosY=y.tolist()
    return datosX,datosY

# Función para determinar los hashtag populares
def hashTagPopular(dfHashtag):
    cantidadTweetsRTPopular=dfHashtag.query('RETWEETS > 500')
    cantidadTweetsRTNormal=dfHashtag.query('RETWEETS <= 500')
    cRTP=cantidadTweetsRTPopular['DATE'].count()
    cRTP=int(cRTP)
    cRTN=cantidadTweetsRTNormal['DATE'].count()
    cRTN=int(cRTN)
    rangosRT=[]
    rangosRT.append(cRTP)
    rangosRT.append(cRTN)
    datosY=rangosRT
    datosX=['POPULAR', 'NORMAL']
    return datosX,datosY

# Función para seleccionar los hashtag más repetidos
def hashtagMoreRepetitive(dfHashtag):
    hashtagRepetidos=dfHashtag
    headhashtagRepetidos=hashtagRepetidos.head(10)
    x=headhashtagRepetidos['HASHTAG']
    y=headhashtagRepetidos['FRECUENCIA']
    datosX=x.tolist()
    datosY=y.tolist()
    return datosX,datosY

# Función para determinar las relación entre Hashtag utilizados y número de RT
def scatterRTvsHashtag(dfHashtag):
    x=dfHashtag['CANT HASHTAG']
    y=dfHashtag['RETWEETS']
    datosX=x.tolist()
    datosY=y.tolist()
    return datosX,datosY
