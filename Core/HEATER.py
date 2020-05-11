from Logger import *

class HEATER:

	__defaultTemp = None

	def __init__(self, object, loggerName):
		self.lg = Logger("syslog.LOG", loggerName +" | HEATER")
		self.__defaultTemp = object.attrib["defaultTemp"]
		self.lg.info("Created")