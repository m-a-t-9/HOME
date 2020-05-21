

class ManageObject:

	def __init__(self, logger):
		self.lg = logger

	def dump(self):
		self.lg.info("DUMP: " + str(self.__dict__))
