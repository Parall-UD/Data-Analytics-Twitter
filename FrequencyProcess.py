# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:31:33 2018

@author: Andres
"""

import pandas as pd

#----------------- Frecuencia de Palabras--------------------------------------
# palabras que se deben retirar de las plabras de los texto, dado que no tienen significado
def asignarPalabrasVac():
    palabrasvac = ['ÉL', 'ÉSTA', 'ÉSTAS', 'ÉSTE', 'ÉSTOS','EL', 'ESTA', 'ESTAS', 'ESTE', 'ESTOS']
    palabrasvac += ['ÚLTIMA', 'ÚLTIMAS', 'ÚLTIMO', 'ÚLTIMOS', 'ULTIMA', 'ULTIMAS', 'ULTIMO', 'ULTIMOS']
    palabrasvac += ['A', 'AÑADIÓ', 'AÚN', 'ACTUALMENTE', 'ADELANTE', 'AÑADIO']
    palabrasvac += ['ADEMÁS', 'AFIRMÓ', 'AGREGÓ', 'AHÍ', 'AHORA', 'AL', 'ADEMAS', 'AFIRMO', 'AGREGO', 'AHI']
    palabrasvac += ['ALGÚN', 'ALGO', 'ALGUNA', 'ALGUNAS', 'ALGUNO', 'ALGUNOS', 'ALGUN']
    palabrasvac += ['ALREDEDOR', 'AMBOS', 'ANTE', 'ANTERIOR', 'ANTES',]
    palabrasvac += ['APENAS', 'APROXIMADAMENTE', 'AQUÍ', 'ASÍ', 'AQUI', 'ASI']
    palabrasvac += ['ASEGURÓ', 'AUNQUE', 'AYER', 'BAJO', 'BIEN', 'BUEN', 'ASEGURO']
    palabrasvac += ['BUENA', 'BUENAS', 'BUENO', 'BUENOS', 'CÓMO', 'CADA']
    palabrasvac += ['CASI', 'CERCA', 'CIERTO', 'CINCO', 'COMENTÓ', 'COMO', 'COMENTO']
    palabrasvac += ['CON', 'CONOCER', 'CONSIDERÓ', 'CONSIDERA', 'CONTRA','CONSIDERO']
    palabrasvac += ['COSAS', 'CREO', 'CUAL', 'CUALES', 'CUALQUIER', 'CUANDO']
    palabrasvac += ['CUANTO', 'CUATRO', 'CUENTA', 'DA', 'DADO', 'DAN', 'DAR']
    palabrasvac += ['DE', 'DEBE', 'DEBEN', 'DEBIDO', 'DECIR', 'DEJÓ', 'DEL','DEJO']
    palabrasvac += ['DEMÁS', 'DENTRO', 'DESDE', 'DESPUÉS', 'DICE', 'DICEN','DEMAS' ,'DESPUES']
    palabrasvac += ['DICHO', 'DIERON', 'DIFERENTE', 'DIFERENTES', 'DIJERON']
    palabrasvac += ['DIJO', 'DIO', 'DONDE', 'DOS', 'DURANTE', 'E', 'EJEMPLO']
    palabrasvac += ['EL', 'ELLA', 'ELLAS', 'ELLO', 'ELLOS', 'EMBARGO', 'EN']
    palabrasvac += ['ENCUENTRA', 'ENTONCES', 'ENTRE', 'ERA', 'ERAN', 'ES']
    palabrasvac += ['ESA', 'ESAS', 'ESE', 'ESO', 'ESOS', 'ESTÁ', 'ESTÁN', 'ESTA', 'ESTAN']
    palabrasvac += ['ESTABA', 'ESTABAN', 'ESTAMOS', 'ESTAR', 'ESTARÁ', 'ESTAS', 'ESTARA']
    palabrasvac += ['ESTE', 'ESTO', 'ESTOS', 'ESTOY', 'ESTUVO', 'EX', 'EXISTE']
    palabrasvac += ['EXISTEN', 'EXPLICÓ', 'EXPRESÓ', 'FIN', 'FUE', 'FUERA' , 'EXPLICO', 'EXPRESO']
    palabrasvac += ['FUERON', 'GRAN', 'GRANDES', 'HA', 'HABÍA', 'HABÍAN' , 'HABIA', 'HABIAN']
    palabrasvac += ['HABER', 'HABRÁ', 'HACE', 'HACEN', 'HACER', 'HACERLO', 'HABRA']
    palabrasvac += ['HACIA', 'HACIENDO', 'HAN', 'HASTA', 'HAY', 'HAYA']
    palabrasvac += ['HE', 'HECHO', 'HEMOS', 'HICIERON', 'HIZO', 'HOY']
    palabrasvac += ['HUBO', 'IGUAL', 'INCLUSO', 'INDICÓ', 'INFORMÓ', 'INFORMO']
    palabrasvac += ['JUNTO', 'LA', 'LADO', 'LAS', 'LE', 'LES', 'LLEGÓ', 'LLEGO']
    palabrasvac += ['LLEVA', 'LLEVAR', 'LO', 'LOS', 'LUEGO', 'LUGAR']
    palabrasvac += ['MÁS', 'MANERA', 'MANIFESTÓ', 'MAYOR', 'ME', 'MEDIANTE', 'MANIFESTO']
    palabrasvac += ['MEJOR', 'MENCIONÓ', 'MENOS', 'MI', 'MIENTRAS', 'MISMA', 'MENCIONO']
    palabrasvac += ['MISMAS', 'MISMO', 'MISMOS', 'MOMENTO', 'MUCHA', 'MUCHAS']
    palabrasvac += ['MUCHO', 'MUCHOS', 'MUY', 'NADA', 'NADIE', 'NI', 'NINGÚN' , 'NINGUN']
    palabrasvac += ['NINGUNA', 'NINGUNAS', 'NINGUNO', 'NINGUNOS', 'NO', 'NOS']
    palabrasvac += ['NOSOTRAS', 'NOSOTROS', 'NUESTRA', 'NUESTRAS', 'NUESTRO']
    palabrasvac += ['NUESTROS', 'NUEVA', 'NUEVAS', 'NUEVO', 'NUEVOS', 'NUNCA']
    palabrasvac += ['O', 'OCHO', 'OTRA', 'OTRAS', 'OTRO', 'OTROS', 'PARA']
    palabrasvac += ['PARECE', 'PARTE', 'PARTIR', 'PASADA', 'PASADO', 'PERO']
    palabrasvac += ['PESAR', 'POCA', 'POCAS', 'POCO', 'POCOS', 'PODEMOS']
    palabrasvac += ['PODRÁ', 'PODRÁN', 'PODRÍA', 'PODRÍAN', 'PONER', 'POR', 'PODRA', 'PODRAN', 'PODRIA', 'PODRIAN']
    palabrasvac += ['PORQUE', 'POSIBLE', 'PRÓXIMO', 'PRÓXIMOS', 'PRIMER' , 'PROXIMO', 'PROXIMOS']
    palabrasvac += ['PRIMERA', 'PRIMERO', 'PRIMEROS', 'PRINCIPALMENTE', 'PROPIA']
    palabrasvac += ['PROPIAS', 'PROPIO', 'PROPIOS', 'PUDO', 'PUEDA']
    palabrasvac += ['PUEDE', 'PUEDEN', 'PUES', 'QUÉ', 'QUE', 'QUEDÓ', 'QUEDO']
    palabrasvac += ['QUEREMOS', 'QUIÉN', 'QUIEN', 'QUIENES', 'QUIERE']
    palabrasvac += ['REALIZÓ', 'REALIZADO', 'REALIZAR', 'RESPECTO', 'SÍ','REALIZO']
    palabrasvac += ['SÓLO', 'SE', 'SEÑALÓ', 'SEA', 'SEAN', 'SEGÚN', 'SEGUNDA', 'SOLO']
    palabrasvac += ['SEGUNDO', 'SEIS', 'SER', 'SERÁ', 'SERÁN', 'SERÍA', 'SI' , 'SERA', 'SERAN', 'SERIA']
    palabrasvac += ['SIDO', 'SIEMPRE', 'SIENDO', 'SIETE', 'SIGUE', 'SIGUIENTE']
    palabrasvac += ['SIN', 'SINO', 'SOBRE', 'SOLA', 'SOLAMENTE', 'SOLAS', 'SOLO']
    palabrasvac += ['SOLOS', 'SON', 'SU', 'SUS', 'TAL', 'TAMBIÉN', 'TAMPOCO' , 'TAMBIEN']
    palabrasvac += ['TAN', 'TANTO', 'TENÍA', 'TENDRÁ', 'TENDRÁN', 'TENEMOS' , 'TENIA', 'TENDRA', 'TENDRAN']
    palabrasvac += ['TENER', 'TENGA', 'TENGO', 'TENIDO', 'TERCERA', 'TIENE']
    palabrasvac += ['TIENEN', 'TODA', 'TODAS', 'TODAVÍA', 'TODO', 'TODOS', 'TODAVIA']
    palabrasvac += ['TOTAL', 'TRAS', 'TRATA', 'TRAVÉS', 'TRES', 'TUVO' , 'TRAVES']
    palabrasvac += ['UN', 'UNA', 'UNAS', 'UNO', 'UNOS', 'USTED', 'VA']
    palabrasvac += ['VAMOS', 'VAN', 'VARIAS', 'VARIOS', 'VECES', 'VER']
    palabrasvac += ['VEZ', 'Y', 'YA', 'YO',')','(',',','.','#','@','TU','TÚ','TE','DO','TO', 'MI' , 'ME', 'DE', 'MÁS', 'MAS']
    palabrasvac += ['THE', 'AND', 'OF', 'IN', 'IS', 'OUR', 'FOR', 'A', 'E', 'I', 'O', 'U', '|','*','+', '-']

    return palabrasvac

# palabras que se deben retirar de los hashtag dado que no tienen significados
def asignarpalabrasvacHashtag():
    palabrasvacHashtag = ['NAN','TBT','NANNAN','...,','NONE']
    return palabrasvacHashtag

# Localiza la posición de la columna TEXT en el dataframe
def funcLocText(dtf):
    for i in range(len(dtf.columns)):
        if dtf.columns[i] == 'TEXT':
            posicion=i;
    return posicion

#Ordena el diccionario de palabras de mayor a menor frecuencia
def ordenarDicc(diccionario):
    aux=[(diccionario[key],key) for key in diccionario]
    aux.sort()
    aux.reverse()
    return dict(aux)

# Limpia y alista el texto para ser procesado
def alistarTexto(dataframe):
    cadenaPalabrasUno=""
    valorPos=int(funcLocText(dataframe))
    for r in range(dataframe['TEXT'].count()):
        cadenaPalabrasUno+=str(dataframe.iloc[r,valorPos])
    cad=cadenaPalabrasUno.replace(",","").replace(".","").replace(":","").replace("#","").replace("@","").replace(";","").replace("!","").replace("?","")
    cadenaPalabras = cad.upper();
    cadenaPalabras = cadenaPalabras.replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
    listaPalabras = cadenaPalabras.split()
    listaPalabrasCompleta=quitarPalabrasvac(listaPalabras,asignarPalabrasVac())
    varDiccionario=listaPalabrasDicFrec(listaPalabrasCompleta)
    varDiccionario=ordenarDicc(varDiccionario)
    arregloKeyPalabra=[]
    arregloValueFrecuencia=[]
    for key, value in varDiccionario.items():
        aKey=key
        aValue=value
        arregloKeyPalabra.append(aKey)
        arregloValueFrecuencia.append(aValue)
    palabrasDict=pd.DataFrame(data=arregloValueFrecuencia,columns=['PALABRA'])
    frecuenciasDict=pd.DataFrame(data=arregloKeyPalabra,columns=['FRECUENCIA'])
    framePalabras=[palabrasDict,frecuenciasDict]
    frecuenciaPalabras=pd.concat(framePalabras,axis=1)
    return frecuenciaPalabras

# Esta función eliminar las palabras sin significado de las palabras del texto
def quitarPalabrasvac(listaPalabras, palabrasvac):
    return [w for w in listaPalabras if w not in palabrasvac]

# Diccionario de frencuencia de palabras
def listaPalabrasDicFrec(listaPalabrasCompleta):
    frecuenciaPalab = [listaPalabrasCompleta.count(w) for w in listaPalabrasCompleta] # a list comprehension
    return dict(zip(listaPalabrasCompleta,frecuenciaPalab))

#-----------------Frecuencia de Hashtag -------------------------------
# Obtiene la posición donde se encuentran los hashtag
def obtenerPos(df):
    nCol=df['CANT HASHTAG'].max()
    arrNomHash=[]
    arrPosHash=[]
    for i in range(nCol):
        arrNomHash.append('HASHTAG'+str(i))
    for i in range(len(arrNomHash)):
        for j in range(len(df.columns)):
            if df.columns[j] == arrNomHash[i]:
                arrPosHash.append(j)
                break;
    return arrPosHash

# Hace el tratamiento de Hashtag
def tratatHashtag(df):
    #palabrasvacHashtag = [element.upper() for element in asignarpalabrasvacHashtag()]
    cadena=''
    arra=[]
    frecuenciaNoHash=[]
    nuevodf=df[df['CANT HASHTAG']>0]
    if nuevodf.empty:
        frecuenciaNoHash=pd.DataFrame(arra)
        return frecuenciaNoHash
    else:
        cantRows=nuevodf['CANT HASHTAG'].count()
        arregloPosicionHash=obtenerPos(nuevodf)
        for i in range(len(arregloPosicionHash)):
            for r in range(cantRows):
                cadena+=str(nuevodf.iloc[r,arregloPosicionHash[i]])
                cadena+=' '
        cad=cadena.replace(',','').replace('.','')
        cadenaPalabras = cad.upper();
        cadenaPalabras = cadenaPalabras.replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
        listaPalabras = cadenaPalabras.split()
        listaPalabrasCompleta=quitarPalabrasvac(listaPalabras,asignarpalabrasvacHashtag())
        varDiccionario=listaPalabrasDicFrec(listaPalabrasCompleta)
        arregloKeyPalabra=[]
        arregloValueFrecuencia=[]
        for key, value in varDiccionario.items():
            aKey=key
            aValue=value
            arregloKeyPalabra.append(aKey)
            arregloValueFrecuencia.append(aValue)
        palabrasDict=pd.DataFrame(data=arregloKeyPalabra,columns=['HASHTAG'])
        frecuenciasDict=pd.DataFrame(data=arregloValueFrecuencia,columns=['FRECUENCIA'])
        frameHash=[palabrasDict,frecuenciasDict]
        freHash=pd.concat(frameHash,axis=1)
        frecuenciaHash=freHash.sort_values('FRECUENCIA',ascending=False)
        return frecuenciaHash
