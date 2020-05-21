from .Logger import *
from .ManageObject import *
from .ENERGY import *
from .WEATHER import *

class MEASUREMENT(ManageObject):

	def __init__(self):
		self.lg = Logger("syslog.LOG", "MEASUREMENT")
		self.__energy = ENERGY()
		self.__weather = WEATHER()

	def getEnergyObject(self):
		return self.__energy

	def getWeatherObject(self):
		return self.__weather