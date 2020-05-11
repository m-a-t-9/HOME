import threading

from Logger import *
from WINDOW import *
from HEATER import *
from MODULE import *
class ROOM:

	__name = ''
	__expectedTemp = None
	__currentTemp = None
	__windows = []
	__heater = None
	__module = None

	def __init__(self, object):
		self.lg = Logger("syslog.LOG", "ROOM")
		self.__initialize(object)

	def __initialize(self, object):
		self.__name = object.attrib['name']
		self.__expectedTemp = object.attrib['expectedTemp']
		self.lg.setComponent("ROOM ["+self.__name+"]")
		self.__configureComponents(object)
		self.lg.info("__initialize: Configuration DONE")

	def __configureComponents(self, object):
		for child in object:
			if child.tag == "WINDOW":
				self.__windows.append(WINDOW(child, self.lg.getComponent()))
			elif child.tag == "HEATER":
				self.__heater = HEATER(child, self.lg.getComponent())
			elif child.tag == "MODULE":
				self.__connectToModule(child)

	def __connectToModule(self, object):
		self.__module = MODULE(object)
		self.__module.connect()
		if self.__module.getState() == MODULE.getStates()["CONNECTED"]:
			self.lg.info("Room is connected to network")
			self.__getDataAboutRoom()
			self.__startMonitoring()

	def __getDataAboutRoom(self):
		self.__module.sendCommand("GET_TEMPERATURE")
		
	def setupTemperature(self, value):
		'''
		Documentation:
		External interface, call by upper layers
		'''
		self.lg.info("Trying to set temperature to: " + str(value))
		self.__module.sendCommand("SET_TEMPERATURE", [value])

	def getTemperature(self):
		return self.__currentTemp

	def __startMonitoring(self):
		thread = threading.Thread(target=self.__observeTemperature, args=())
		thread.daemon = True
		thread.start()


	def __observeTemperature(self):
		while True:
			self.__setTemperature(self.__module.sendCommand("GET_TEMPERATURE"))
			time.sleep(60)

	def __setTemperature(self, value):
		self.lg.info(" current temperature in room is: " + value)
		self.__currentTemp = value
