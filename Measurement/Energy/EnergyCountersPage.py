from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class EnergyCountersPage:

	def __init__(self, driver):
		self.driver = driver
		self.checkboxOZE = driver.find_element(By.CSS_SELECTOR, "input[id='checkOZE']")
		self.checkboxOZE.click()
		time.sleep(4)
		self.chartOZEValue = driver.find_element(By.CSS_SELECTOR, "span[id='chartOZEValue']")
		self.chartValue = driver.find_element(By.XPATH, "span[id='chartValue']")

	def getOZEValue(self):
		return self.chartOZEValue.text

	def getValue(self):
		return self.chartValue.text

	def selectYearlyTab(self):
		self.yearTabElement = self.driver.find_element(By.CSS_SELECTOR, "//a[contains(text(), 'Rok')]")
		self.yearTabElement.click()

	def getOZEValueForYear(self):
		self.selectYearlyTab()
		self.checkboxOZE = self.driver.find_element(By.CSS_SELECTOR, "input[id='checkOZE']")
		self.checkboxOZE.click()
		time.sleep(4)
		self.chartOZEValue = driver.find_element(By.CSS_SELECTOR, "span[id='chartOZEValue']")
		return self.chartOZEValue.text
