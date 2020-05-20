import datetime

class Logger:

	def __init__(self, filename, component):
		self.__filename = filename
		self.__component = component

	def start(self):
		f = open(self.__filename, "a")
		f.write("********************************************************************\n")
		f.close()

	def info(self, msg, attribs=[]):
		f = open(self.__filename, "a")
		row = self.__getDate() + " | INFO | " + self.__component + " | " + msg + "\n"
		for attrib in attribs:
			row += attrib + "\n"
		f.write(row)
		f.close()

	def error(self, msg, attribs=[]):
		f = open(self.__filename, "a")
		row = self.__getDate() + " | ERROR | " + self.__component + " | " + msg + "\n"
		for attrib in attribs:
			row += attrib + "\n"
		f.write(row)
		f.close()

	def __getDate(self):
		return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

	def setComponent(self, name):
		self.__component = name

	def getComponent(self):
		return self.__component
	