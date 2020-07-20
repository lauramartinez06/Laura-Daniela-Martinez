print("PRINCIPIOS SOLID")
'''
Principio de Responsabilidad unica
'''
class Motorcycles:
	def __init__(self,color):
		self.color = color
	def get_Motorcycles_color(self):
		return self.color()

class MotorcyclesDB:
	"""Base de datos"""
	def save_Motorcycles_DB(self,Motorcycles):
		return Motorcycles()

	def delete_Motorcycles_DB(self,Motorcycles)
		return 'Motorcycles deleted'

main()







		

		