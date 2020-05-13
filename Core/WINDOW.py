from .Logger import *
from .BLIND import *
class WINDOW:
	
	__id = None
	__blind = None

	def __init__(self, object, loggerName):
		self.lg = Logger("syslog.LOG", loggerName)
		self.__initialize(object)

	def __initialize(self, object):
		self.__id = object.attrib['id']
		if len(object) > 0:
			self.__initializeBlinds(object)
		self.lg.info("WINDOW [" + self.__id + "] | __initialize: Configuration DONE")

	def __initializeBlinds(self, object):
		for child in object:
			if child.tag == "BLIND":
				self.__blind = BLIND(self.lg.getComponent())