from TauronPage import *

tauronPage = TauronPage()
tauronPage.login()
tauronPage.connectToEnergyCounters()

print("Produced: " + tauronPage.getProducedEnergyAmount())
print("Consumed: " + tauronPage.getConsumedEnergyAmount())
print("Produced in this year: " + tauronPage.getProducedEnergyAmountInYear())

#tauronPage.teardown()
