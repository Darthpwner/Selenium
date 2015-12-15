#Selenium Python testing framework
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 

class SeleniumPythonTest:
	def __init__(self, driver, url):
		self.url = url
		self.driver = driver
		driver.maximize_window()
	def searchForXpath(locator):
		WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(locator))
	def searchForCssSelector():
		WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(locator))
