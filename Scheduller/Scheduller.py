from .Logger import *

class Scheduller:

	def __init__(self, modelHandler):
		self.lg = Logger("syslog.LOG", "Scheduller")
		self.mH = modelHandler
		self.lg.info("Scheduller: __init__")