from selenium import webdriver

import unittest

from TravelingTony.Constants import TT_Constants


class BaseTestCase(object):

  def setUp(self):
      if TT_Constants['Browser'].lower() == "firefox":
      	 self.driver = webdriver.Firefox()
         #self.driver.maximize_window()
      elif TT_Constants['Browser'].lower() == "chrome":
      	 self.driver = webdriver.Chrome()
         #self.driver.maximize_window()
      elif TT_Constants['Browser'].lower() == "ie": 
         self.driver = webdriver.Ie()
         #self.driver.maximize_window()
      else:
      	raise Exception("This browser is not supported at the moment.")

  def navigate_to_page(self, url):
      self.driver.get(url)

  def tearDown(self):
  	  self.driver.quit()
