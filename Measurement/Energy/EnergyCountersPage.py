from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime


class EnergyCountersPage:

	def __init__(self, driver):
		self.driver = driver
		self.checkboxOZE = driver.find_element(By.CSS_SELECTOR, "input[id='checkOZE']")
		self.checkboxOZE.click()
		time.sleep(4)
		self.chartOZEValue = driver.find_element(By.CSS_SELECTOR, "span[id='chartOZEValue']")
		self.chartValue = driver.find_element(By.CSS_SELECTOR, "span[id='chartValue']")

	def getOZEValue(self):
		return self.chartOZEValue.text

	def getValue(self):
		return self.chartValue.text

	def selectYearlyTab(self):
		self.yearTabElement = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Rok')]")
		self.yearTabElement.click()

	def getOZEValueForYear(self):
		self.selectYearlyTab()
		self.checkboxOZE = self.driver.find_element(By.CSS_SELECTOR, "input[id='checkOZE']")
		time.sleep(5)
		self.checkboxOZE.click()
		time.sleep(4)
		self.chartOZEValue = self.driver.find_element(By.CSS_SELECTOR, "span[id='chartOZEValue']")
		return self.chartOZEValue.text


	def getDailyAverageValue(self):
		self.selectDailyTab()
		return self.getMyAverageValue()

	def selectDailyTab(self):
		self.dayTabElement = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Dzień')]")
		self.dayTabElement.click()
		self.checkboxAverageValue = self.driver.find_element(By.CSS_SELECTOR, "input[id='checkMyAverage']")
		self.checkboxAverageValue.click()
		time.sleep(4)


	def getMyAverageValue(self):
		self.lastNumberOfdays = self.driver.find_element(By.XPATH, "//div[@class='lastValue']/input")
		day_of_year = datetime.now().timetuple().tm_yday
		self.lastNumberOfdays.clear()
		self.lastNumberOfdays.send_keys(str(day_of_year-1))
		self.lastNumberOfdays.send_keys(Keys.ENTER)
		time.sleep(4)
		self.chartMyAverageValue = self.driver.find_element(By.CSS_SELECTOR, "span[id='chartMyAverageValue']")
		return self.chartMyAverageValue.text