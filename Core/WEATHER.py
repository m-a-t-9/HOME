from .ManageObject import *
from .Logger import *

class WEATHER(ManageObject):

	__minTemp = ""
	__maxTemp = ""
	__descritpion = ""

	def __init__(self):
		self.lg = Logger("syslog.LOG", "WEATHER")

