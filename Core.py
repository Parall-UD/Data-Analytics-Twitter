from flask import Flask, render_template, request, jsonify
import DataClean as dc
import DataGenerator as dg
import FrequencyProcess as fp
import AnalysisTemplate as at
from datetime import datetime, date, time, timedelta


app = Flask(__name__)

hoy = datetime.today()  # Asigna fecha-hora
# Asigna formato de la fecha
formato1 = "%Y-%m-%d"
parametros=[]

dates=[str((hoy-timedelta(days=6)).strftime(formato1)),str((hoy-timedelta(days=5)).strftime(formato1)),str((hoy-timedelta(days=4)).strftime(formato1)),str((hoy-timedelta(days=3)).strftime(formato1)),str((hoy-timedelta(days=2)).strftime(formato1)),str((hoy-timedelta(days=1)).strftime(formato1)),str(hoy.strftime(formato1))]
print(dates)

@app.route('/')
def index():
	return render_template('principal.html')

@app.route('/manuales')
def manuales():
	return render_template('manuales.html')

@app.route('/process', methods=['POST'])
def process():
    parametros=[]
    contenido = request.form
    diccionarioContenido=contenido.copy()

    for i in range(len(diccionarioContenido)):
        parametros.append(diccionarioContenido[str(i)])

    tipoBusqueda=parametros.pop()
    tipoFiltro=parametros.pop()

    if (tipoBusqueda == 'AND'):
		#compendio por conjunción
        dataFrameFinal, estadoConsulta = dg.generarCompendioAND(dg.separateParameters(parametros),dates,tipoFiltro)
    else:
		#comprendio por disyunción
        dataFrameFinal, estadoConsulta = dg.generarCompendioOR(parametros,dates,tipoFiltro)

    if (estadoConsulta):
        dataFrameFrecuencyWords=fp.alistarTexto(dataFrameFinal)
        dataFrameFrecuencyHashtag=fp.tratatHashtag(dataFrameFinal)
        arregloUnoX,arregloUnoY=at.wordsMoreRepetitive(dataFrameFrecuencyWords)
        arregloDosX,arregloDosY=at.hashtagMoreRepetitive(dataFrameFrecuencyHashtag)
        arregloTresX,arregloTresY=at.hashTagPopular(dataFrameFinal)
        arregloCuatroX, arregloCuatroY = at.scatterRTvsHashtag(dataFrameFinal)

	# De acuerdo al estado de la consulta se enviar la respuesta a JS, donde se pasa por medio de un JSON
    if (estadoConsulta) :
        parametros=[]
        return jsonify({ 'resultX1' :  arregloUnoX , 'resultY1' :  arregloUnoY , 'resultX2' :  arregloDosX , 'resultY2' :  arregloDosY , 'resultX3' :  arregloTresX , 'resultY3' :  arregloTresY , 'resultX4' :  arregloCuatroX , 'resultY4' :  arregloCuatroY })
    else:
        parametros=[]
        return jsonify({'error' : 'Los términos no arrojaron resultados!'})



if __name__ == '__main__':
	app.run(debug=False)
