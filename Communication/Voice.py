from gtts import gTTS
import playsound
import speech_recognition as sr
import threading


class Voice:

	__filename=""
	__recognizer=None
	__source = None
	__listening = False
	__activated = False
	__enabled = True

	def __init__(self):
		self.__filename = "output.mp3"
		self.__recognizer = sr.Recognizer()
		#with sr.Microphone() as self.__source:
		#	

	def say(self, text):
		if self.__enabled:
			tts = gTTS(text, lang='pl')
			tts.save(self.__filename)
			playsound.playsound(self.__filename, True)	

	def getSayHandler(self):
		return self.say

	def disable(self):
		self.__enabled = False

	def startListening(self):
		thread = threading.Thread(target=self.__listen, args=())
		thread.daemon = True
		self.__listening = True
		thread.start()

	def __listen(self):
		while self.__listening:
			with sr.Microphone() as source:
				self.__recognizer.adjust_for_ambient_noise(source)
				try:
					audio = self.__recognizer.listen(source)
					text = self.__recognizer.recognize_google(audio, "pl-PL")
					print(text)
					if not self.__activated:
						if text == "hej":
							self.__activated = True
							self.say("Cześć, co tam?: ")
					else:
						print(text)
						self.say("zrozumiałem: " + text)
				except sr.UnknownValueError:
				    self.say("Nie zrozumiałem, czy możesz powtórzyć")
				except sr.RequestError as e:
				    self.say("Wystąpił problem: " + format(e))
				except sr.WaitTimeoutError as e:
					print("Timeout")
				except e:
					print (e)