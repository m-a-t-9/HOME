from .Logger import *
from .ROOM import *
from .MEASUREMENT import *
from .ManageObject import *

STATES = ["", "UNCONFIGURED", "CONFIGURED"]

class HOME(ManageObject):

	__address = ""
	__name = ""
	__owner = ""
	__type = 0
	__state = STATES[0]
	__MEASUREMENT = None


	def __init__(self, logger, object):
		self.__rooms = []
		self.lg = Logger("syslog.LOG", "HOME")
		self.__initialize(object)

	def getRooms(self):
		return self.__rooms

	def addRoom(self, room):
		self.__rooms.append(room)

	def __initialize(self, object):
		if object == None:
			self.__state = STATES[1]
			self.lg.error("__initialize: HOME is UNCONFIGURED")
			return
		for prop in object.attrib:
			if prop == "address":
				self.__address = object.attrib[prop]
			elif prop == "name":
				self.__name = object.attrib[prop]
			elif prop == "owner":
				self.__owner = object.attrib[prop]
			elif prop == "type":
				self.__type = object.attrib[prop]
		self.__loadRooms(object)
		#self.__initializeDoors(object.find("DOOR"))
		self.__startMeasurement()
		self.lg.info("__initialize: HOME is CONFIGURED")

	def __loadRooms(self, object):
		for child in object:
			if child.tag == "ROOM":
				self.addRoom(ROOM(child))

	def __startMeasurement(self):
		self.__MEASUREMENT = MEASUREMENT()

	def getEnergyObject(self):
		return self.__MEASUREMENT.getEnergyObject()

	def getWeatherObject(self):
		return self.__MEASUREMENT.getWeatherObject()

	
		