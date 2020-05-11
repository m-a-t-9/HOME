from Logger import *
from ROOM import *

STATES = ["", "UNCONFIGURED", "CONFIGURED"]

class HOME:

	__address = ""
	__name = ""
	__owner = ""
	__type = 0
	__state = STATES[0]

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
		self.__initializeDoors(object.find("DOOR"))
		self.lg.info("__initialize: HOME is CONFIGURED")

	def __loadRooms(self, object):
		for child in object:
			if child.tag == "ROOM":
				self.addRoom(ROOM(child))
