from Communication import Voice
from Core import *




def main():
	lg = Logger.Logger("syslog.LOG", "ROOT")
	lg.start()
	voiceService = Voice.Voice()
	voiceService.say("System został zresetowany poprawnie")
	lg.info("SYSTEM STARTED")
	model = Model.Model()
	voiceService.startListening()
	while True:
		pass

if __name__ == '__main__':
	main()