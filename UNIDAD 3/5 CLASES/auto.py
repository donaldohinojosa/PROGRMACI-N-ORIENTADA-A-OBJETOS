class Auto:
	color = "verde"
	Placas ="AAL-126"
	Alarma = False
	gTotal= 0

	def _init_(self,e,f):
		self.gastokm = e
		self.distancia = f


		def calculo(self):
			self.gTotal= self.gastokm * self.distancia



			def imprime_consumo(self):
				print("El gasto por Km es de"+str (self.gastokm))
				print("La distancia es:" +str (self.distancia))
				print("El gasto total fue de:" +str (self.gTotal))





chevy = Auto(12,100)
chevy.calculo()
chevy.imprime_consumo()