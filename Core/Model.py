from .HOME import *
import xml.etree.ElementTree as ET
from .Logger import *

class Model:

	__tree = None
	__root = None	

	def __init__(self):
		self.lg = Logger("syslog.LOG", "Model")
		self.__loadModel()
		self.__home = HOME(self.lg, self.__root)

	def __loadModel(self):
		try:
			self.__tree = ET.parse('model.xml')
			self.__root = self.__tree.getroot()
			self.lg.info("__loadModel: Model parsed")
		except:
			self.lg.error("__loadModel: Cannot parse model")

	def getHome(self):
		return self.__home

	def interface(self, message):
		pass

	def getModelHandler(self):
		return self.interface