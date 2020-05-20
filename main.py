from Communication import Voice
from Core import *
from Scheduller import *



def main():
	lg = Logger.Logger("syslog.LOG", "ROOT")
	lg.start()
	voiceService = Voice.Voice()
	voiceService.say("System został zresetowany poprawnie")
	lg.info("SYSTEM STARTED")
	model = Model.Model()
	scheduller = Scheduller.Scheduller(model.getModelHandler())
	voiceService.startListening()
	while True:
		pass

if __name__ == '__main__':
	main()