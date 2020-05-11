from Logger import *
STATES = {"OPENED": 1, "CLOSED": 2}

class BLIND:

	__state = None
	__percentage = None

	def __init__(self, loggerName):
		self.lg = Logger("syslog.LOG", loggerName + " | BLIND")
		self.lg.info("Created")

	def openBlind(self):
		self.lg.info("Blind is opening")
		self.__state = STATES["OPENED"]

	def closeBlind(self):
		self.lg.info("Blind is closing")
		self.__state = STATES["CLOSED"]
