from Communication import Voice
from Core import *
from Scheduller import *



def main():
	lg = Logger.Logger("syslog.LOG", "ROOT")
	lg.start()
	voiceService = Voice.Voice()
	voiceService.disable()
	voiceService.say("System został zresetowany poprawnie")
	lg.info("SYSTEM STARTED")
	scheduleService = Scheduller.Scheduller()
	model = Model.Model(voiceService.getSayHandler(), scheduleService.getInterface())	
	scheduleService.runTriggers()
	voiceService.startListening()
	
	while True:
		pass

if __name__ == '__main__':
	main()