class Operaciones:


	def __init__(self,numero1,numero2):
		self.numero1 = numero1
		self.numero2 = numero2

	def Suma(self, numero1, numero2):
		if numero1 == None or numero2 == None :
			return None

		resultado = numero1 + numero2	
		return resultado

	def Resta(self, numero1, numero2):
		if numero1 == None or numero2 == None :
			return None

		resultado = numero1 - numero2
		return resultado

	def Multiplicacion(self, numero1, numero2):
		if numero1 == None or numero2 == None :
			return None

		resultado = numero1*numero2
		return resultado

	def Division(self, numero1,numero2):
		if numero1 == None or numero2 == None :
			return None
		resultado = numero1/numero2
		return resultado

	def Potencia(self, numero1,numero2):
		if numero1 == None or numero2 == None :
			return None

		resultado = pow(numero1,numero2)
		return resultado

	def Raiz(self, numero1,numero2):
		if numero1 == None or numero2 == None :
			return None

		pot = 1/numero2	

		resultado = pow(numero1,pot)
		return resultado



