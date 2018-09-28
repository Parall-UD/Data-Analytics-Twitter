# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:35:49 2018

@author: Andres
"""

import pandas as pd

# Extrae la columna fecha del json  y genera la columna de fecha del nuevo dataframe
def generarDate(g):
    created_dateArreglo=[]
    for h in range(len(g)):
        created_dateArreglo.append(g[h]['created_at'])
    columnaCreated_date=pd.DataFrame(created_dateArreglo,columns=['DATE'])
    return columnaCreated_date

# Extrae la columna name del json  y genera la columna de name del nuevo dataframe
def generarName(g):
    NameArreglo=[]
    for i in range(len(g)):
        NameArreglo.append(g[i]['user']['name'])
    columnaName=pd.DataFrame(NameArreglo,columns=['NAME'])
    return columnaName

# Extrae la columna screenname del json  y genera la columna de screenname del nuevo dataframe
def generarScreenName(g):
    screenNameArreglo=[]
    for j in range(len(g)):
        screenNameArreglo.append(g[j]['user']['screen_name'])
    columnaScreenName=pd.DataFrame(screenNameArreglo,columns=['SCREEN_NAME'])
    return columnaScreenName

# Extrae la columna location del json  y genera la columna de location del nuevo dataframe
def generarLocation(g):
    locationArreglo=[]
    for k in range(len(g)):
        locationArreglo.append(g[k]['user']['location'])
    columnaLocation=pd.DataFrame(locationArreglo,columns=['LOCATION'])
    return columnaLocation

# Extrae la columna Retweets del json  y genera la columna de Retweets del nuevo dataframe
def generarRetweets(g):
    retweetsArreglo=[]
    for k in range(len(g)):
        retweetsArreglo.append(g[k]['retweet_count'])
    columnaRetweetCount=pd.DataFrame(retweetsArreglo,columns=['RETWEETS'])
    return columnaRetweetCount

# Extrae la columna full text del json  y genera la columna de text del nuevo dataframe
def generarText(g):
    textArreglo=[]
    for k in range(len(g)):
        textArreglo.append(g[k]['full_text'])
    columnaText=pd.DataFrame(textArreglo,columns=['TEXT'])
    return columnaText

# Extrae los hashtag del json  y genera la columna de hashtag del nuevo dataframe
# Extrae la cantidad de hashtag contando los hashtag extraidos anteriormente
def generarHashtag(g):
    hashtags=[]
    hashtagsAux=[]
    contadorHashtags=0;
    contadorHashtagArreglo=[]
    for m in range(len(g)):
        hashtagsAux=[]
        if(g[m]['entities']['hashtags']!= []):
            #print('ENTRE IF')
            for n in range(len(g[m]['entities']['hashtags'])):
                hashtagsAux.append(g[m]['entities']['hashtags'][n]['text'])
                contadorHashtags=contadorHashtags+1
            contadorHashtagArreglo.append(contadorHashtags)
            hashtags.append(hashtagsAux)
            hashtagsAux=[]

        else:
            contadorHashtags=0;
            contadorHashtagArreglo.append(contadorHashtags)
            hashtags.append(hashtagsAux)
    hashtagsDos=[]
    hashArrelo=[]
    hashArregloLen=[]
    for l in range (len(hashtags)):
        hashArregloLen.append(len(hashtags[l]))
    numeroColHash=max(hashArregloLen)
    if numeroColHash!=0:
        for u in range(numeroColHash):
            etiquetaHash="HASHTAG"+str(u)
            hashArrelo.append(etiquetaHash)
        columnaHashtags=pd.DataFrame(hashtags,columns=hashArrelo)
    elif numeroColHash==0:
        for o in range(len(g)):
            hashtagsDos.append('')
        for t in range((numeroColHash+1)):
            etiquetaHash="HASHTAG"+str(t)
            hashArrelo.append(etiquetaHash)
            columnaHashtags=pd.DataFrame(hashtagsDos,columns=['HASHTAG0'])
    columnaNumHashtag=pd.DataFrame(contadorHashtagArreglo,columns=['CANT HASHTAG'])
    return columnaHashtags, columnaNumHashtag

def tratamientoDeDatos(g):
    columnaCreated_date=generarDate(g)
    columnaName=generarName(g)
    columnaScreenName=generarScreenName(g)
    columnaLocation=generarLocation(g)
    columnaRetweetCount=generarRetweets(g)
    columnaText=generarText(g)
    columnaHashtags,columnaNumHashtag = generarHashtag(g)
    frames=[columnaCreated_date,columnaName,columnaScreenName,columnaText,columnaLocation,columnaNumHashtag,columnaHashtags,columnaRetweetCount]
    dfFinal= pd.concat(frames, axis=1)
    return dfFinal
