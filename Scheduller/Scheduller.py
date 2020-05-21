from .Logger import *
from .Trigger import *

import threading
from datetime import datetime
import time
import xml.etree.ElementTree as ET

class Scheduller:

	__triggers = []
	__tree = None

	def __init__(self):
		self.lg = Logger("syslog.LOG", "Scheduller")
		self.lg.info("Scheduller: __init__")
		#self.__loadTriggers()
		#self.__runTrigger()

	def __loadTriggers(self):
		#to be removed
		self.__tree = ET.parse('Triggers.xml')
		self.__root = self.__tree.getroot()	
		for element in self.__root.findall("TRIGGER"):
			self.__triggers.append(Trigger(name=element.attrib['name'], path=element.attrib['path'], freq=element.attrib['when']))
		self.lg.info("Triggers loaded and schedulled")

	def runTriggers(self):
		self.__triggersThread= threading.Thread(target=self.__run, daemon=True)
		self.__triggersThread.start()

	def __run(self):
		while True:
			for trigger in self.__triggers:
				self.lg.info("Check trigger: " + trigger.getName())
				if trigger.getNextExecution() == datetime.now().strftime('%d/%m/%Y') and not trigger.hasBeenExecuted():
					trigger.run()
				self.lg.info("Next please")
			self.lg.info("Next round please")
			time.sleep(120)

	def __interface(self, command):
		#["ADD_TRIGGER", ["name", "path", "when", "reportingPlace"]]
		#["ENFORCED_TRIGGER", ["name"]]
		action = command[0]
		arg = command[1]
		if action == "ADD_TRIGGER":
			self.lg.info("Adding new Trigger " + arg[0])
			self.__triggers.append(Trigger(name=arg[0], path=arg[1], freq=arg[2], resultObj=arg[3]))
		elif action == "ENFORCED_TRIGGER":
			self.lg.info("Enforced Trigger " + arg[0])
			for trigger in self.__triggers:
				if trigger.getName() == arg[0]:
					trigger.run()
					return

	def getInterface(self):
		return self.__interface