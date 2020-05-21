from .ManageObject import *
from .Logger import *

class ENERGY(ManageObject):

	__produced = ""
	__consumed = ""
	__averageDailyConsumption = ""

	def __init__(self):
		self.lg = Logger("syslog.LOG","ENERGY")
