from TauronPage import *

tauronPage = TauronPage()
tauronPage.login()s
tauronPage.connectToEnergyCounters()

print("Produced: " + tauronPage.getProducedEnergyAmount())
print("Consumed: " + tauronPage.getConsumedEnergyAmount())
print("Produced in this year: " + tauronPage.getProducedEnergyAmountInYear())
print("Average daily consumption: "+ tauronPage.getAverageDailyConsumption())

#tauronPage.teardown()
