#Selenium Python testing framework
from selenium                                       import webdriver
from selenium.webdriver.support.ui                  import WebDriverWait
from selenium.webdriver.common.by                   import By
from selenium.webdriver.common.action_chains        import ActionChains
from selenium.webdriver.common.keys                 import Keys

import unittest
import time

class SeleniumPythonTest(unittest.TestCase):	#Inherits from unittest.TestCase
	#Init method
	# def __init__(self, driver, url):
	# 	self.url = url
	# 	self.driver = driver
	# 	driver.maximize_window()
	#

	#Set up browser
	def useFirefox():
		driver = webdriver.Firefox()
	def useChrome():
		driver = webdriver.Chrome()
	#

	#Search methods
	def searchForXpath(locator):
		WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(locator))
	def searchForCssSelector(locator):
		WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(locator))
	#

	#SearchAndClick methods
	def searchAndClickBasedOnXpath(locator):
		buttonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(locator))	#Searches based on xpath
		buttonElement.click()
	def searchAndClickBasedOnCssSelector(locator):
		buttonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(locator))	#Searches based on CSS selector
		buttonElement.click()
	#