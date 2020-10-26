from Operaciones import Operaciones
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Historial import Historial

historial = []

op = Operaciones

app = Flask(__name__)

CORS(app)


@app.route('/suma', methods = ['POST'])

def suma():

	if request.method == 'POST' :

		response = {}

		A = request.form.get('numero1')
		B = request.form.get('numero2')

		if op.Suma(A,B) is not None :
			response['estado'] = 1
			response['resultado'] = resultado
			historial.append(Historial(A,B,"+",resultado))
		response['estado'] = 0
		return response	


@app.route('/resta', methods = ['POST'])

def resta():

	if request.method == 'POST' :

		response = {}

		A = request.form.get('numero1')
		B = request.form.get('numero2')

		if op.Resta(A,B) is not None :
			response['estado'] = 1
			response['resultado'] = resultado
			historial.append(Historial(A,B,"-",resultado))
		response['estado'] = 0
		return response


@app.route('/multiplicacion', methods =['POST'])

def multiplicacion():

	if request.method == 'POST' :

		response = {}

		A = request.form.get('numero1')
		B = request.form.get('numero2')

		if op.Multiplicacion(A,B) is not None :
			response['estado'] = 1
			response['resultado'] = resultado
			historial.append(Historial(A,B,"*",resultado))
		response['estado'] = 0
		return response	

@app.route('/division', methods = ['POST'])

def division():
	
	if request.method == 'POST':

		response = {}

		A = request.form.get('numero1')
		B = request.form.get('numero2')

		if op.Division(A,B) is not None :
			response['estado'] = 1
			response['resultado'] = resultado
			historial.append(Historial(A,B,"/",resultado))
		response['estado'] = 0
		return response	
		

@app.route('/potencia',methods = ['POST'])

def potencia():
	 
	if request.method == 'POST':

		response = {}

		A = request.form.get('numero1')
		B = request.form.get('numero2')

		if op.Potencia(A,B) is not None :
			response['estado'] = 1
			response['resultado'] = resultado
			historial.append(Historial(A,B,"^",resultado))
			response['estado'] = 0
			return response	

@app.route('/Raiz', methods = ['POST'])
def Raiz():

	if request.method == 'POST':

		response = {}

		A = request.form.get('numero1')
		B = request.form.get('numero2')

		if op.Raiz(A,B) is not None :
			response['estado'] = 1
			response['resultado'] = resultado
			historial.append(Historial(A,B,"raiz",resultado))
		response['estado'] = 0
		return response	


@app.route('/<name>')

def index(name):
	return render_template("calculadora.html",name = "calculadora") 

if __name__ == '__main__':
	app.run(threaded=True, port=500,debug=True)	


