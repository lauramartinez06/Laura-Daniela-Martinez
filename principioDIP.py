'''
Principio de Inversión de dependencia
'''
class ConnectionInterface():
	def get_data(self):
		pass

	def save_data(self)
		pass

class ServiceDatabase (ConnectionInterface)
	def get_data(self):
	return 'Information from database'
	def save_data(self):
		return 'Data has been saved'

class APIService(ConnectionInterface):

	def get_data(self):
		return 'Information from database'

	def save_data(self):
		return 'Data has been saved'

main()
	
		
