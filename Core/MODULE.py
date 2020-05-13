from .Logger import *
import socket
import threading
import time

STATES = {"DISCONNECTED":0, "CONNECTED":1, "FAILED":2}

class MODULE:

	__ip = ''
	__port = 12345
	__state = STATES['DISCONNECTED']
	__socket = None
	__WELCOME_MESSAGE = 'Hello, HOME here'

	def __init__(self, object):
		self.setIp(object.attrib['ip'])
		self.lg = Logger("syslog.LOG", "MODULE [" + self.getIp() + "]")
		

	def setIp(self, ip):
		self.__ip = ip

	def getIp(self):
		return self.__ip

		
	def getState(self):
		return self.__state

	def getStates():
		return STATES

	def connect(self):
		self.lg.info("Trying to connect to module")
		try:
			self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.__socket.connect((self.__ip, self.__port))
			self.__socket.send(self.__WELCOME_MESSAGE.encode())
			data = self.__socket.recv(1024).decode()
			if data.find("Hello, MODULE") != -1:
				self.__state = STATES['CONNECTED']
				self.lg.info("State has been changed to value: CONNECTED")
			elif data.find("Exit, MODULE") != -1:
				self.__state = STATES['DISCONNECTED']
				self.lg.error("State has been changed to value: DISCONNECTED")
		except Exception as e:
			self.__state = STATES["FAILED"]
			self.lg.error("State has been changed to value: FAILED: " + str(e))

	def sendCommand(self, command, args = []):
		for arg in args:
			command += "_" + arg
		self.__socket.send(command.encode())
		self.lg.info("sendCommand performed successfully. Waiting for response")
		data = self.__socket.recv(1024).decode()
		return data

	def __parseResponse(self, data):
		pass