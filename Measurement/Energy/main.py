from TauronPage import *

tauronPage = TauronPage()
tauronPage.login()
tauronPage.connectToEnergyCounters()

produced = tauronPage.getProducedEnergyAmount()
consumed = tauronPage.getConsumedEnergyAmount()
averageDailyConsumed =  tauronPage.getAverageDailyConsumption()

print('[{"produced":"' + str(produced) + '","consumed":"' + str(consumed) + '","averageDailyConsumption":"'+ str(averageDailyConsumed)+ '"}]')
#print("Consumed: " + )
#print("Produced in this year: " + tauronPage.getProducedEnergyAmountInYear())
#print("Average daily consumption: "+)

tauronPage.teardown()
