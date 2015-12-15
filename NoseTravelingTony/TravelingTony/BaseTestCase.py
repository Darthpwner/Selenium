from selenium import webdriver

import unittest

from TravelingTony.Constants import TT_Constants

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BaseTestCase(object):

  def setUp(self):
      capabilities = {} #Create an empty dictionary
      if TT_Constants['Browser'].lower() == "firefox":
          capabilities = DesiredCapabilities.FIREFOX.copy()
          capabilities['platform'] = "MAC"
          capabilities['version'] = "30.0"
          self.driver = webdriver.Remote(desired_capabilities=capabilities, 
                                        command_executor="http://localhost:4444/wd/hub"
          )
      	 # self.driver = webdriver.Firefox()
         #self.driver.maximize_window()
      elif TT_Constants['Browser'].lower() == "chrome":
      	  capabilities = DesiredCapabilities.CHROME.copy()
          capabilities['platform'] = "MAC"
          self.driver = webdriver.Remote(desired_capabilities=capabilities, 
                                        command_executor="http://localhost:4444/wd/hub"
          )
         #self.driver = webdriver.Chrome()
         #self.driver.maximize_window()
      elif TT_Constants['Browser'].lower() == "ie": 
          capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
          capabilities['platform'] = "WINDOWS"
          capabilities['version'] = "9"
          self.driver = webdriver.Remote(desired_capabilities=capabilities, 
                                        command_executor="http://localhost:4444/wd/hub"
          )
         #self.driver = webdriver.Ie()
         #self.driver.maximize_window()
      else:
      	raise Exception("This browser is not supported at the moment.")

  def navigate_to_page(self, url):
      self.driver.get(url)

  def tearDown(self):
  	  self.driver.quit()
