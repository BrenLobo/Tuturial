class perro():
	#constructor 
	def __init__(self, nombre, color):
		self.color = color
		self.name = nombre
	def corre(self):
		print(str(self.name)+" Esta corriendo")

	def kk(self, a):
		print(str(self.name)+" hizo "+str(a)+"kg de kk")

perro1 = perro("Yuki", "blanco")
perro1.corre()
perro1.kk(7)


perro2 = perro("Amaya", "nigga")
perro2.corre()
perro2.kk(2)