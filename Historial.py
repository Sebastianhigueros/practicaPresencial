from datetime import datetime
import json
class Historial:

	def __init__(self, numero1, numero2, operacion,resultado):
		self.fecha = datetime.datetime.now()
		self.numero1 = numero1
		self.numero2 = numero2
		self.operacion =operacion


	def dump(self):
		return {
			'fecha' : self.fecha,
			'numero1' : self.numero1,
			'numero2' : self.numero2,
			'operacion': self.operacion

		}
