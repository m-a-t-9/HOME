from .Logger import *
import subprocess
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

import threading

class Trigger:

	__name=""
	__path=""
	__occurence=None
	__time=""
	__nextExecution=None
	__executed=False

	def __init__(self, name, path, freq, resultObj):
		self.__name = name
		self.__path = path
		self.__time = freq.split(" ")[0]
		self.__occurence = freq.split(" ")[1]
		#To be enabled when model can return every object in HOME
		self.__resultObj = resultObj
		self.lg = Logger("syslog.LOG", "Trigger ["+self.__name+"]")
		self.__nextExecution = datetime.now().strftime('%d/%m/%Y')

	def run(self):
		try:
			r =subprocess.check_output(["python3", self.__path]).decode()
			self.lg.info("json received: "+r)
			jsonedResponse = json.loads(r)
			for element in jsonedResponse[0]:
				setattr(self.__resultObj, "__" + element, jsonedResponse[0][element])
			self.__resultObj.dump()
			self.__calculateNextExecution()
		except subprocess.CalledProcessError as e:
			self.lg.error("thrown error: " + repr(e))

	def getNextExecution(self):
		return self.__nextExecution

	def __calculateNextExecution(self):
		if (self.__occurence == "DAILY"):
			self.__nextExecution = (datetime.now() + relativedelta(days=1)).strftime('%d/%m/%Y') 
			self.lg.info("next execution calculated to: " + self.__nextExecution)
			self.__executed = True
			t = threading.Timer(5.0, self.__resetExecutionState)
			t.start()

	def __resetExecutionState(self):
			self.__executed = False

	def hasBeenExecuted(self):
		return self.__executed

	def getName(self):
		return self.__name
