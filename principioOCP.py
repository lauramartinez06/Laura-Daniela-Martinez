'''
Principio OCP
'''
class Motorcycles:
	def avg_Motorcycles_model(self):
		pass

class Green(Motorcycles):
	def avg_Motorcycles_model(self):
		return 2012

class Red(Motorcycles):
	def avg_Motorcycles_model():
		return 2016

class Purple(Motorcycles):
	def avg_Motorcycles_model():
		return 2019

class Yellow(Motorcycles):
	def avg_Motorcycles_model():
		return 2020

#Recibo de caja
def print_avg_Motorcycle_model(Motorcycles):
	for Motorcycles in Motorcycles:
		print(Motorcycles.avg_Motorcycles_model())
def main():
	Motorcycles_Green = Green()
	Motorcycles_Red = Red()
	Motorcycles_Purple = Purle()
	Motorcycles_Yellow = Yellow ()

print_avg_Motorcycle_model(Motorcycles)

main()



		