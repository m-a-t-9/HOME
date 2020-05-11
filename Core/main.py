from Logger import *

from Model import *


def main():
	lg = Logger("syslog.LOG", "ROOT")
	lg.start()
	lg.info("SYSTEM STARTED")
	model = Model()
	while True:
		pass

if __name__ == '__main__':
	main()