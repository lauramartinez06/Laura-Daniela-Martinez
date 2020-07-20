'''
Principio de Liskov
'''
class Motorcycles:
def avg_Motorcyles_model(self):
	pass

def avg_Motorcyles_quantity_changes():
	pass

class Green(Motorcycles):
	def avg_Motorcyles_model(self):
		return 2012

	def avg_Motorcyles_quantity_changes(self):
		return 5

class Red(Motorcycles):
	def avg_Motorcyles_model(self):
		return 2016

	def avg_Motorcyles_quantity_changes(self):
		return 4

class Purple(Motorcycles):
	def avg_Motorcyles_model(self):
		return 2019

	def avg_Motorcyles_quantity_changes(self):
		return 6

class Yellow(Motorcyles):
	def avg_Motorcyles_model(self):
		return 2020

	def avg_Motorcyles_quantity_changes():
		return 5

def main():

	Motorcycles_Green = Green()
	Motorcycles_Red = Red()
	Motorcycles_Purple = Purple()
	Motorcycles_Yellow = Yellow()

	Motorcycles = [Motorcycles_Green, Motorcycles_Red, Motorcycles_Purple, Motorcycles_Yellow]

print_avg_Motorcycles_model(Motorcycles)

main()

		
		
				
		