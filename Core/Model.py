from .HOME import *
import xml.etree.ElementTree as ET
from .Logger import *

class Model:

	__tree = None
	__root = None	

	def __init__(self, sayHandler,scheduller):
		self.lg = Logger("syslog.LOG", "Model")
		self.__say = sayHandler
		self.__scheduller = scheduller
		self.__loadModel()
		self.__home = HOME(self.lg, self.__root)
		self.__runExternalInterfaces()


	def __loadModel(self):
		try:
			self.__tree = ET.parse('model.xml')
			self.__root = self.__tree.getroot()
			self.lg.info("__loadModel: Model parsed")
			self.__say("Dzień dobry " + self.__root.attrib['owner'])
		except:
			self.lg.error("__loadModel: Cannot parse model")

	def getHome(self):
		return self.__home

	def __runExternalInterfaces(self):
		self.lg.info("Schedulling Energy power monitoring")
		self.__scheduller(["ADD_TRIGGER", ["Tauron", "/home/mateusz/Projects/HOME/Measurement/Energy/main.py", "9:00 DAILY", self.__home.getEnergyObject()]])
		self.__scheduller(["ADD_TRIGGER", ["Weather", "/home/mateusz/Projects/HOME/Measurement/Climate/main.py", "9:00 DAILY", self.__home.getWeatherObject()]])