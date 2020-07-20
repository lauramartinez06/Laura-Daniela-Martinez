'''
Principio de Segregacion de Interfaces
'''
class AutoInterface():
	def service(self):
		return 'I can service!'

class FastAutoInterface():
	def speed(self):
		return 'I can speed!'

class StrongAutoInterface():
	def force(self):
		return 'I can force'



class Jeep(AutoInterface, StrongAutoInterface):
	def service(self):
		return 'I can service¡`

	def force(self):
		return 'I can force'

class Ferrari(AutoInterface, FastAutoInterface):
	def service(self):
		return 'I can service'

	def speed(self)
	return 'I can speed'

def main()
	
	Jeep = Jeep()
	print (f'Jeep: {Jeep.service()} and { Jeep.force()} ')

	Ferrari = Ferrari()
	print (f'Ferrari: { Ferrari.service() } and { Ferrari.speed()} ')

	main()
	




		
		
	
		

		
	