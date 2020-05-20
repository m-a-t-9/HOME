from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from EnergyCountersPage import *
import time

class TauronPage:

	def __init__(self):
		self.loadProperties()
		self.driver = webdriver.Chrome()
		self.driver.get(self.url)


	def loadProperties(self):
		f = open("Energy.properties", "r")
		self.properties = f.readlines()
		f.close()
		self.url = self.properties[0].split(" ")[1].replace("\n", "")
		self.username = self.properties[1].split(" ")[1].replace("\n", "")
		self.password = self.properties[2].split(" ")[1].replace("\n", "")

	def login(self):
		usernameInput = self.driver.find_element_by_name("username")
		usernameInput.clear()
		usernameInput.send_keys(self.username)
		passwordInput = self.driver.find_element_by_name("password")
		passwordInput.clear()
		passwordInput.send_keys(self.password)
		loginButton = self.driver.find_element(By.CSS_SELECTOR, "a[title='Zaloguj się']")
		loginButton.click()

	def connectToEnergyCounters(self):
		if self.driver.title.find("eLicznik") != -1:
			print("Nothing to be done")
		else:
			buttonToConnect = self.driver.find_element(By.CSS_SELECTOR, self.properties[3].split(" ")[1].replace("\n", ""))
			buttonToConnect.click()
		self.energyCounterPage = EnergyCountersPage(self.driver)

	def getProducedEnergyAmount(self):
		return self.energyCounterPage.getOZEValue()

	def getConsumedEnergyAmount(self):
		return self.energyCounterPage.getValue()

	def getProducedEnergyAmountInYear(self):
		return self.energyCounterPage.getOZEValueForYear()

	def getAverageDailyConsumption(self):
		return self.energyCounterPage.getDailyAverageValue()

	def teardown(self):
		self.driver.close()




